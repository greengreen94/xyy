import pandas as pd
import pymysql
import warnings

# 忽略警告（不推荐，但可以临时使用）
warnings.filterwarnings("ignore", category=UserWarning)

# 数据库连接
conn = pymysql.connect(
    host='10.0.102.52',
    user='root',
    password='123456',
    database='collection',
    charset='utf8mb4'
)

# 执行查询并导出
query = """
SELECT * 
FROM announcement_pingbiao 
WHERE origin_text LIKE '%电话%'
   OR origin_text LIKE '%联系方式%'
LIMIT 10000
"""

df = pd.read_sql(query, conn)
df.to_csv('pingbiao.csv', index=False, encoding='utf-8-sig')
print("导出完成：pingbiao.csv")

conn.close()