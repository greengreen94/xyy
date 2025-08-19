# 合同签订表建立
# public_resources_info_deduplicated   gov_procurement_info1_deduplicated  announcement_deduplicated
# announcement_kaibiao_deduplicated  announcement_pingbiao_deduplicated  announcement_zhongbiao_deduplicated
# gov_procurement_info1_20250609_deduplicated、public_resources_info_20250609_deduplicated

# announcement_20250609_deduplicated  announcement_kaibiao_20250609_deduplicated
# announcement_pingbiao_20250609_deduplicated   announcement_zhongbiao_20250609_deduplicated
import pymysql
from tqdm import tqdm
import os

# 配置：源表和目标表
SOURCE_TABLE = os.getenv("SOURCE_TABLE", "default_table_name")
print(f"当前处理表：{SOURCE_TABLE}")
TARGET_TABLE = "contract_signing"
# 数据库连接配置
conn_src = pymysql.connect(
    host='10.0.102.52', user='root', password='123456',
    database='collection', charset='utf8mb4'
)
conn_dst = pymysql.connect(
    host='10.0.102.52', user='root', password='123456',
    database='construction', charset='utf8mb4'
)

cursor_src = conn_src.cursor(pymysql.cursors.DictCursor)
cursor_dst = conn_dst.cursor()

# 获取当前目标表的最大 ID，空则为 0
cursor_dst.execute(f"SELECT MAX(id) FROM {TARGET_TABLE}")
result = cursor_dst.fetchone()
current_id = result[0] if result[0] is not None else 0

# 分批查询参数
batch_size = 5000
cursor_src.execute(f"""
    SELECT COUNT(*) FROM {SOURCE_TABLE}
    where project_name like '%合同签订%'
""")
total_rows = cursor_src.fetchone()['COUNT(*)']
total_batches = (total_rows + batch_size - 1) // batch_size

# 字段映射
field_mapping = {
    'project_name':'project_name',
    'origin_text': 'origin_text',
    'website': 'source_address',
    'create_time': 'created_time',
    'update_time': 'updated_time'  ##announcement_deduplicated pingbiao
    # 可以继续扩展
}

# 批处理插入
for batch_num in tqdm(range(total_batches), desc=f"分批插入 {TARGET_TABLE}"):
    offset = batch_num * batch_size
    cursor_src.execute(f"""
        SELECT * FROM {SOURCE_TABLE}
        where project_name like '%合同签订%'
        LIMIT {batch_size} OFFSET {offset}
    """)
    rows = cursor_src.fetchall()

    for row in rows:
        columns = ['id']
        current_id += 1
        values = [current_id]

        for src_field, dst_fields in field_mapping.items():
            if src_field in row:
                if isinstance(dst_fields, list):
                    for dst_field in dst_fields:
                        columns.append(dst_field)
                        values.append(row[src_field])
                else:
                    columns.append(dst_fields)
                    values.append(row[src_field])

        placeholders = ','.join(['%s'] * len(values))
        sql = f"INSERT INTO {TARGET_TABLE} ({','.join(columns)}) VALUES ({placeholders})"
        try:
            cursor_dst.execute(sql, values)
        except Exception as e:
            print(f"插入失败: {e}\n数据: {row}")

    conn_dst.commit()

# 关闭连接
cursor_src.close()
cursor_dst.close()
conn_src.close()
conn_dst.close()