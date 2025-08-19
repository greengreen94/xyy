import pandas as pd
from sqlalchemy import create_engine

# 使用 SQLAlchemy 创建引擎（替换你的数据库信息）
engine = create_engine("mysql+pymysql://root:123456@10.0.102.52/collection?charset=utf8mb4")

query = """
SELECT * 
FROM announcement_kaibiao 
WHERE origin_text LIKE '%安徽江淮汽车集团股份有限公司%'
   OR origin_text LIKE '%杭州量知数据科技有限公司%'
   OR origin_text LIKE '%珠海格力电器股份有限公司%'
   OR origin_text LIKE '%浙江大学医学院附属第二医院%'
"""

df = pd.read_sql(query, engine)  # 使用 engine 代替 conn
df.to_csv('announcement_kaibiao.csv', index=False, encoding='utf-8-sig')
print("导出完成：announcement_kaibiao.csv")

# 无需手动关闭 engine（SQLAlchemy 会自动管理连接）