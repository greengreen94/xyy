import pandas as pd
import pymysql

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
FROM announcement_kaibiao 
WHERE origin_text LIKE '%安徽江淮汽车集团股份有限公司%'
   OR origin_text LIKE '%杭州量知数据科技有限公司%'
   OR origin_text LIKE '%珠海格力电器股份有限公司%'
   OR origin_text LIKE '%浙江大学医学院附属第二医院%'
"""

df = pd.read_sql(query, conn)
df.to_csv('pingbiao.csv', index=False, encoding='utf-8-sig')
print("导出完成：pingbiao.csv")

conn.close()