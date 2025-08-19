import pymysql

# 配置信息 - 请根据实际情况修改
SOURCE_CONFIG = {
    'host': '10.0.102.52',
    'port': 3306,  # 源数据库端口，如果不是默认3306请修改
    'user': 'root',  # 源数据库用户名
    'password': '123456',  # 源数据库密码
    'database': 'collection', #
    'table': 'science_zhswxqkw' # 修改 announcement、announcement_kaibiao、announcement_pingbiao、announcement_zhongbiao
    # articles_cailianshe、articles_citreportCom、articles_dczj、articles_itzj、articles_kkj、articles_lzw、articles_MDPI
    # articles_mts、articles_PLOS、articles_shjsw、articles_shyqw、articles_swg、articles_techcrunchCom、articles_techIfengCom
    # articles_xjw、articles_zczx、articles_zggkw、articles_zgyqfzw、articles_zhidxCom
    # beijing_patent_info、bulletin_data、CNIPA_zhuanli、enterprise_dimension、enterprise_info_new、expert_info
    # expert_notice、gov_procurement_info1、gyhxxhhb、hqw、id_tracking、ieee_articles、illegal_enterprises
    # lens_zhuanli、lhgmyhfzhy、lhgxw、patent_info、patent_info_old、public_resources_info、pubscholar_lunwen
    # pubscholar_zhuanli、qianyanzixun_data、qianyanzixun_test、report_199IT、report_eastmoney
    # report_worldbank、SciELO、science_cogentoa、science_cpsjournals、science_DOAJ、science_f1000research
    # science_frontiers、science_jstage、science_knowledge_unlatched、science_opticsjournal
    # science_osf、science_zglxqkw、science_zhswxqkw

    # science_light、source_collection_info、task、TechRxiv
    # uspto_zhuanli、zgzfw、zhaobiao
    # Lost connection to MySQL server during query ([WinError 10054] 远程主机强迫关闭了一个现有的连接。)：articles_MDPI、articles_PLOS
}

TARGET_CONFIG = {
    'host': '203.83.233.7',
    'port': 3307,  # 目标数据库端口，如果不是默认3306请修改
    'user': 'root',  # 目标数据库用户名
    'password': 'AIIT2025',  # 目标数据库密码
    'database': 'aiit_collection',
    'table': 'science_zhswxqkw'
}

BATCH_SIZE = 1000  # 每次批量处理的数据量
LIMIT = 10000  # 总共要复制的数据量


def copy_data():
    try:
        # 连接源数据库
        source_conn = pymysql.connect(
            host=SOURCE_CONFIG['host'],
            port=SOURCE_CONFIG['port'],
            user=SOURCE_CONFIG['user'],
            password=SOURCE_CONFIG['password'],
            database=SOURCE_CONFIG['database'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # 连接目标数据库
        target_conn = pymysql.connect(
            host=TARGET_CONFIG['host'],
            port=TARGET_CONFIG['port'],
            user=TARGET_CONFIG['user'],
            password=TARGET_CONFIG['password'],
            database=TARGET_CONFIG['database'],
            charset='utf8mb4'
        )

        with source_conn.cursor() as source_cursor, target_conn.cursor() as target_cursor:
            # 获取源表结构
            source_cursor.execute(f"SHOW CREATE TABLE {SOURCE_CONFIG['table']}")
            create_table_sql = source_cursor.fetchone()['Create Table']

            # 修改表名为目标表名
            create_table_sql = create_table_sql.replace(
                f"CREATE TABLE `{SOURCE_CONFIG['table']}`",
                f"CREATE TABLE IF NOT EXISTS `{TARGET_CONFIG['table']}`"
            )

            # 在目标数据库创建表
            target_cursor.execute(create_table_sql)

            # 分批复制数据
            offset = 0
            total_copied = 0

            while total_copied < LIMIT:
                current_batch = min(BATCH_SIZE, LIMIT - total_copied)

                # 从源表读取数据
                source_cursor.execute(
                    f"SELECT * FROM {SOURCE_CONFIG['table']} LIMIT {offset}, {current_batch}"
                )
                batch_data = source_cursor.fetchall()

                if not batch_data:
                    break  # 没有更多数据了

                # 准备插入语句
                columns = list(batch_data[0].keys())
                placeholders = ', '.join(['%s'] * len(columns))
                columns_str = '`, `'.join(columns)

                insert_sql = (
                    f"INSERT INTO `{TARGET_CONFIG['table']}` (`{columns_str}`) "
                    f"VALUES ({placeholders})"
                )

                # 插入到目标表
                target_cursor.executemany(
                    insert_sql,
                    [tuple(row.values()) for row in batch_data]
                )

                total_copied += len(batch_data)
                offset += current_batch

                print(f"已复制 {total_copied}/{LIMIT} 条记录")

                # 提交当前批次
                target_conn.commit()

        print(f"数据复制完成，共复制 {total_copied} 条记录")

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        if 'source_conn' in locals() and source_conn:
            source_conn.close()
        if 'target_conn' in locals() and target_conn:
            target_conn.close()


if __name__ == "__main__":
    copy_data()