import pymysql
from pymysql import Error


def transfer_origin_text():
    # 初始化连接和游标
    connection = None
    cursor = None

    try:
        # 1. 建立数据库连接
        connection = pymysql.connect(
            host='10.0.102.52',  # 数据库主机地址
            user='root',  # 数据库用户名
            password='123456',  # 数据库密码
            database='construction',  # 数据库名
            charset='utf8mb4',  # 字符集（避免中文乱码）
            cursorclass=pymysql.cursors.DictCursor  # 返回字典格式数据
        )

        # 2. 执行数据转移
        with connection.cursor() as cursor:
            # 从 bid_result_publicity 查询数据
            select_sql = "SELECT origin_text FROM bid_result_publicity"
            cursor.execute(select_sql)
            origin_texts = cursor.fetchall()  # 获取所有记录

            # 插入到 product_new_copy1
            insert_sql = "INSERT INTO product_new_copy1 (origin_text) VALUES (%s)"
            # 提取 origin_text 字段值（PyMySQL返回字典格式）
            data_to_insert = [(item['origin_text'],) for item in origin_texts]

            # 批量插入
            cursor.executemany(insert_sql, data_to_insert)
            connection.commit()  # 提交事务

        print(f"成功插入 {len(data_to_insert)} 条数据！")

    except Error as e:
        print(f"数据库错误: {e}")
        if connection:
            connection.rollback()  # 出错时回滚

    finally:
        # 关闭连接
        if connection:
            connection.close()
            print("数据库连接已关闭")


# 执行函数
transfer_origin_text()