import pandas as pd

# 尝试使用不同编码读取CSV文件
encodings = ['utf-8-sig', 'gb18030', 'gbk', 'latin1']

for encoding in encodings:
    try:
        df = pd.read_csv('matched_procurement_data.csv', encoding=encoding)
        print(f"成功使用编码: {encoding}")
        break
    except UnicodeDecodeError:
        continue
else:
    raise ValueError("无法找到合适的编码")

# 继续执行分类代码...
companies = [
    "安徽江淮汽车集团股份有限公司",
    "杭州量知数据科技有限公司",
    "珠海格力电器股份有限公司",
    "浙江大学医学院附属第二医院"
]

for company in companies:
    company_df = df[df['origin_text'].str.contains(company, na=False)]
    if not company_df.empty:
        filename = f"matched_procurement_data_{company}.csv"
        company_df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"已分类保存: {filename}")