import pymysql
from collections import defaultdict
from itertools import groupby

# 数据库连接配置
db_config = {
    'host': '10.0.102.52',
    'user': 'root',
    'password': '123456',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# 从所有表格中整理出的完整数据
classification_data = [
    # 产业报告
    {"分类": "产业报告", "数据库名称": "collection", "mysql表名": "report_eastmoney", "数据是否混合": "否"},
    {"分类": "产业报告", "数据库名称": "collection", "mysql表名": "report_199IT", "数据是否混合": "否"},
    {"分类": "产业报告", "数据库名称": "collection", "mysql表名": "ieee_articles", "数据是否混合": "否"},
    {"分类": "产业报告", "数据库名称": "collection", "mysql表名": "TechRxiv", "数据是否混合": "否"},
    {"分类": "产业报告", "数据库名称": "collection", "mysql表名": "articles_PLOS", "数据是否混合": "否"},
    {"分类": "产业报告", "数据库名称": "collection", "mysql表名": "articles_MDPI", "数据是否混合": "否"},

    # 科技文献和发明专利
    {"分类": "发明专利", "数据库名称": "collection", "mysql表名": "pubscholar_zhuanli", "数据是否混合": "否"},
    {"分类": "科技文献", "数据库名称": "collection", "mysql表名": "pubscholar_lunwen", "数据是否混合": "否"},
    {"分类": "发明专利", "数据库名称": "collection", "mysql表名": "CNIPA_zhuanli", "数据是否混合": "否"},
    {"分类": "发明专利", "数据库名称": "collection", "mysql表名": "uspto_zhuanli", "数据是否混合": "否"},
    {"分类": "发明专利", "数据库名称": "collection", "mysql表名": "lens_zhuanli", "数据是否混合": "否"},

    # 市场分析（招采）
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement_20250707", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement_kaibiao", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement_kaibiao_20250707", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement_zhongbiao", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement_zhongbiao_20250707", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement_pingbiao", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "announcement_pingbiao_20250707", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "public_resources_info", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "public_resources_info_20250630", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "public_resources_info_20250707", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "gov_procurement_info1", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "gov_procurement_info1_20250630", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "gov_procurement_info1_20250707", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "bulletin_data", "数据是否混合": "否"},
    {"分类": "市场分析（招采）", "数据库名称": "collection", "mysql表名": "illegal_enterprises", "数据是否混合": "否"},

    # 国际时事
    {"分类": "国际时事", "数据库名称": "collection", "mysql表名": "hqw", "数据是否混合": "否"},
    {"分类": "国际时事", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.jfdaily.com/'"},
    {"分类": "国际时事", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://zgb.cyol.com/'"},
    {"分类": "国际时事", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://mdaily.yunnan.cn'"},
    {"分类": "国际时事", "数据库名称": "collection", "mysql表名": "lhgxw", "数据是否混合": "否"},

    # 重点事件和政策信息
    {"分类": "重点事件", "数据库名称": "collection", "mysql表名": "zgzfw", "数据是否混合": "否"},
    {"分类": "政策信息", "数据库名称": "collection", "mysql表名": "gyhxxhhb", "数据是否混合": "否"},
    {"分类": "政策信息", "数据库名称": "collection", "mysql表名": "zgzfw", "数据是否混合": "否"},
    {"分类": "政策信息", "数据库名称": "collection", "mysql表名": "lhgmyhfzhy", "数据是否混合": "否"},
    {"分类": "政策信息", "数据库名称": "collection", "mysql表名": "report_worldbank", "数据是否混合": "否"},

    # 舆情民生和企业信息
    {"分类": "舆情民生", "数据库名称": "collection", "mysql表名": "articles_zgyqfzw", "数据是否混合": "否"},
    {"分类": "企业信息", "数据库名称": "collection", "mysql表名": "enterprise_dimension", "数据是否混合": "否"},

    # 咨询研报
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_zggkw", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_itzj", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_cailianshe", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_swg", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_mts", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_lzw", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_dczj", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_xjw", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_techIfengCom", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_zhidxCom", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_citreportCom", "数据是否混合": "否"},
    {"分类": "咨询研报", "数据库名称": "collection", "mysql表名": "articles_techcrunchCom", "数据是否混合": "否"},

    # 量子科技
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.quantumcas.ac.cn'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.qtc.com.cn'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'quantum.phys.tsinghua.edu.cn'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.quantum-info.com'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.ciqtek.com'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'originqc.com.cn'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'quantumconsortium.org'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.nist.gov'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'uwaterloo.ca'"},
    {"分类": "量子科技", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'quantum.ustc.edu.cn'"},

    # 集成电路
    {"分类": "集成电路", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'laoyaoba.com'"},
    {"分类": "集成电路", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.doit.com.cn'"},
    {"分类": "集成电路", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.eetimes.com'"},


    # 新能源
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.irena.org'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.iea.org'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'cleanenergycouncil.org.au'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'arena.gov.au'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.pv-magazine.com'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.energy-storage.news'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'cleantechnica.com'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.nea.gov.cn'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.cnenergynews.cn'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.cpnn.com.cn'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'www.china-nengyuan.com'"},
    {"分类": "新能源", "数据库名称": "collection", "mysql表名": "qianyanzixun_data", "数据是否混合": "是",
     "where condition": "site = 'newenergy.in-en.com'"},
    # ... 其他新能源条件 ...
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://paper.people.com.cn/zgmyb'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'http://www.ceu.zju.edu.cn'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'http://www.baimalakelab.com'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.roche.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.bms.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.astrazeneca.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.gsk.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.modernatx.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.biontech.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.sanofi.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.lilly.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.abbott.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.bayer.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.gilead.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.novartis.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.takeda.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.astellas.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://investor.regeneron.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://chiaic.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.nmed.org.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'http://www.cntmic.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'http://www.nctip.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.nctib.org.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.nctid.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'http://nctisa.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.niicpm.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.cannano.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.cpl.ac.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.gzlab.ac.cn/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.lglab.ac.cn/yjcg/xshd/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.technologyreview.com/'"},
    {"分类": "新能源", "数据库名称": "news", "mysql表名": "daily", "数据是否混合": "是",
     "where condition": "site = 'https://www.chinastarmarket.cn/subject/1279'"}
    # ... 其他新能源条件 ...
]


def count_records_by_classification():
    # 按分类汇总数据量
    classification_counts = defaultdict(int)
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:
            # 先按分类分组，再按表名分组
            sorted_data = sorted(classification_data, key=lambda x: (x['分类'], x['mysql表名'], x['数据库名称']))
            grouped = groupby(sorted_data, key=lambda x: (x['分类'], x['mysql表名'], x['数据库名称']))

            for (classification, table_name, db_name), group in grouped:
                group_items = list(group)
                is_mixed = group_items[0]['数据是否混合'] == '是'

                try:
                    cursor.execute(f"USE {db_name};")

                    if not is_mixed:
                        # 非混合表，直接统计全表
                        query = f"SELECT COUNT(*) AS count FROM {table_name};"
                        cursor.execute(query)
                        result = cursor.fetchone()
                        count = result['count'] if result else 0
                        classification_counts[classification] += count
                        print(f"已统计 {classification} 的 {db_name}.{table_name}: {count} 条记录")
                    else:
                        # 混合表，组合所有条件统计
                        conditions = [item['where condition'] for item in group_items if 'where condition' in item]
                        if conditions:
                            where_clause = " OR ".join([f"({cond})" for cond in conditions])
                            query = f"SELECT COUNT(*) AS count FROM {table_name} WHERE {where_clause};"
                            cursor.execute(query)
                            result = cursor.fetchone()
                            count = result['count'] if result else 0
                            classification_counts[classification] += count
                            print(f"已统计 {classification} 的 {db_name}.{table_name} ({where_clause}): {count} 条记录")

                except Exception as e:
                    print(f"查询 {db_name}.{table_name} 时出错: {e}")
                    continue

    finally:
        connection.close()

    return dict(classification_counts)


if __name__ == "__main__":
    counts = count_records_by_classification()
    print("\n各分类数据量统计结果:")
    for classification, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{classification}: {count:,} 条记录")  # 使用千位分隔符格式化数字