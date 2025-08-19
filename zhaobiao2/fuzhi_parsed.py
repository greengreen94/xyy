import pymysql

# 配置信息 - 请根据实际情况修改
SOURCE_CONFIG = {
    'host': '10.0.102.52',
    'port': 3306,  # 源数据库端口
    'user': 'root',  # 源数据库用户名
    'password': '123456',  # 源数据库密码
    'database': 'parsed_data',
    'table': 'bid_evaluation_event_parsed' # tender_info_parsed、bid_opening_event_parsed、bid_evaluation_event_parsed
}

TARGET_CONFIG = {
    'host': '203.83.233.7',
    'port': 3307,  # 目标数据库端口
    'user': 'root',  # 目标数据库用户名
    'password': 'AIIT2025',  # 目标数据库密码
    'database': 'aiit_collection',
    'table': 'bid_evaluation_event'
}

# 需要排除的字段列表
EXCLUDE_COLUMNS = ['id', 'source_id']  # 不需要导入的字段

BATCH_SIZE = 1000  # 每次批量处理的数据量


def append_data_with_auto_increment():
    try:
        # 连接源数据库（使用字典游标）
        source_conn = pymysql.connect(
            host=SOURCE_CONFIG['host'],
            port=SOURCE_CONFIG['port'],
            user=SOURCE_CONFIG['user'],
            password=SOURCE_CONFIG['password'],
            database=SOURCE_CONFIG['database'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        # 连接目标数据库（也使用字典游标保持一致性）
        target_conn = pymysql.connect(
            host=TARGET_CONFIG['host'],
            port=TARGET_CONFIG['port'],
            user=TARGET_CONFIG['user'],
            password=TARGET_CONFIG['password'],
            database=TARGET_CONFIG['database'],
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with source_conn.cursor() as source_cursor, target_conn.cursor() as target_cursor:
            # 1. 获取目标表当前最大ID（使用字典访问方式）
            target_cursor.execute(f"SELECT COALESCE(MAX(id), 0) AS max_id FROM {TARGET_CONFIG['table']}")
            result = target_cursor.fetchone()
            current_max_id = result['max_id']  # 使用字典键访问
            next_id = current_max_id + 1
            print(f"下一个自动生成的ID将从 {next_id} 开始")

            # 2. 从源表读取数据总数
            source_cursor.execute(f"SELECT COUNT(*) AS cnt FROM {SOURCE_CONFIG['table']}")
            total_records = source_cursor.fetchone()['cnt']  # 使用字典键访问
            print(f"源表共有 {total_records} 条记录待导入")

            # 3. 获取源表列名（排除不需要的列）
            source_cursor.execute(f"SHOW COLUMNS FROM {SOURCE_CONFIG['table']}")
            all_columns = [col['Field'] for col in source_cursor.fetchall()]  # 使用字典键访问
            columns = [col for col in all_columns if col not in EXCLUDE_COLUMNS]
            columns_str = '`, `'.join(columns)
            placeholders = ', '.join(['%s'] * len(columns))

            # 4. 获取目标表列名（用于验证）
            target_cursor.execute(f"SHOW COLUMNS FROM {TARGET_CONFIG['table']}")
            target_columns = [col['Field'] for col in target_cursor.fetchall()]  # 使用字典键访问

            # 检查列是否匹配
            missing_columns = set(columns) - set(target_columns)
            if missing_columns:
                print(f"警告：目标表缺少以下列: {missing_columns}")
                # 可以选择只保留两个表共有的列
                columns = [col for col in columns if col in target_columns]
                columns_str = '`, `'.join(columns)
                placeholders = ', '.join(['%s'] * len(columns))

            # 5. 分批处理数据
            offset = 0
            total_copied = 0

            while True:
                # 从源表读取一批数据
                source_cursor.execute(
                    f"SELECT * FROM {SOURCE_CONFIG['table']} LIMIT {offset}, {BATCH_SIZE}"
                )
                batch_data = source_cursor.fetchall()

                if not batch_data:
                    break  # 没有更多数据了

                # 准备插入数据（只包含需要的列）
                insert_data = []
                for row in batch_data:
                    insert_data.append(tuple(row[col] for col in columns))  # 使用字典键访问

                # 构建并执行插入语句
                insert_sql = f"""
                    INSERT INTO `{TARGET_CONFIG['table']}` (`{columns_str}`) 
                    VALUES ({placeholders})
                """
                target_cursor.executemany(insert_sql, insert_data)

                total_copied += len(batch_data)
                offset += BATCH_SIZE

                print(f"已导入 {total_copied}/{total_records} 条记录")
                target_conn.commit()

        print(f"数据导入完成，共导入 {total_copied} 条记录")

    except Exception as e:
        print(f"发生错误: {str(e)}")
        if 'target_conn' in locals():
            target_conn.rollback()
    finally:
        if 'source_conn' in locals() and source_conn:
            source_conn.close()
        if 'target_conn' in locals() and target_conn:
            target_conn.close()


if __name__ == "__main__":
    append_data_with_auto_increment()