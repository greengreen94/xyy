import pymysql
from tqdm import tqdm


def copy_mysql_table(source_host, source_port, source_user, source_password, source_db, source_table,
                     dest_host, dest_port, dest_user, dest_password, dest_db, dest_table, limit=10000):
    """
    复制MySQL表数据从源到目标

    参数:
        source_host: 10.0.102.52
        source_port: 3306
        source_user: root
        source_password: 123456
        source_db: collection
        source_table: articles_MDPI
        dest_host: 203.83.233.7
        dest_port: 3307
        dest_user: root
        dest_password: AIIT2025
        dest_db: aiit_collection
        dest_table: articles_MDPI
        limit: 10000
    """
    try:
        # 连接到源数据库
        source_conn = pymysql.connect(
            host=source_host,
            port=source_port,
            user=source_user,
            password=source_password,
            db=source_db,
            charset='utf8mb4'
        )

        # 连接到目标数据库
        dest_conn = pymysql.connect(
            host=dest_host,
            port=dest_port,
            user=dest_user,
            password=dest_password,
            db=dest_db,
            charset='utf8mb4'
        )

        with source_conn.cursor() as source_cursor, dest_conn.cursor() as dest_cursor:
            # 获取源表数据
            print(f"从源表 {source_table} 读取前 {limit} 条数据...")
            source_cursor.execute(f"SELECT * FROM {source_table} LIMIT {limit}")
            columns = [desc[0] for desc in source_cursor.description]

            # 准备插入语句
            placeholders = ', '.join(['%s'] * len(columns))
            insert_sql = f"INSERT INTO {dest_table} ({', '.join(columns)}) VALUES ({placeholders})"

            # 分批插入
            print(f"插入到目标表 {dest_table}...")
            batch_size = 500
            batch = []
            inserted_count = 0

            for row in tqdm(source_cursor, total=limit):
                batch.append(row)
                if len(batch) >= batch_size:
                    dest_cursor.executemany(insert_sql, batch)
                    inserted_count += len(batch)
                    batch = []

            if batch:
                dest_cursor.executemany(insert_sql, batch)
                inserted_count += len(batch)

            dest_conn.commit()
            print(f"成功插入 {inserted_count} 条记录到目标表")

    except Exception as e:
        print(f"发生错误: {str(e)}")
        if 'dest_conn' in locals():
            dest_conn.rollback()
    finally:
        if 'source_conn' in locals():
            source_conn.close()
        if 'dest_conn' in locals():
            dest_conn.close()


# 使用示例
if __name__ == "__main__":
    copy_mysql_table(
        source_host="10.0.102.52",
        source_port=3306,  # 替换为实际端口
        source_user="root",  # 替换为实际用户名
        source_password="123456",  # 替换为实际密码
        source_db="collection",
        source_table="articles_MDPI",
        dest_host="203.83.233.7",
        dest_port=3307,  # 替换为实际端口
        dest_user="root",  # 替换为实际用户名
        dest_password="AIIT2025",  # 替换为实际密码
        dest_db="aiit_collection",
        dest_table="articles_MDPI",
        limit=10000
    )
