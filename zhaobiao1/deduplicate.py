import os
import sys
import pymysql
from tqdm import tqdm
from html import unescape
import re

# ========= 获取环境变量 =========
SOURCE_TABLE = os.getenv("RAW_SOURCE_TABLE")
TARGET_TABLE = os.getenv("TARGET_TABLE")

# ========= 检查参数有效性 =========
if not SOURCE_TABLE:
    print("错误：未设置环境变量 RAW_SOURCE_TABLE，请设置数据源表名！")
    sys.exit(1)

if not TARGET_TABLE:
    print("错误：未设置环境变量 TARGET_TABLE，请设置目标表名！")
    sys.exit(1)

# ========= 配置ID记录 =========
ID_RECORD_FILE = f"id_record_{SOURCE_TABLE}.txt"
DEFAULT_START_ID = 0
BATCH_SIZE = 10000
INSERT_BATCH_SIZE = 500

# ============ 表结构配置 ============
TABLE_CONFIG = {
    "announcement": {
        "fields": [
            "id", "task_id", "project_name", "industries", "regions",
            "tender_amount", "website", "acquisition_source", "origin_text",
            "analytic_result", "release_time", "end_time", "path",
            "create_time", "update_time", "announcement_type"
        ]
    },
    "announcement_kaibiao": {
        "fields": [
            "id", "task_id", "project_name", "industries", "regions",
            "announcement_type", "website", "acquisition_source",
            "origin_text", "analytic_result", "receive_time",
            "path", "create_time", "update_time"
        ]
    },
    "announcement_pingbiao": {
        "fields": [
            "id", "task_id", "project_name", "industries", "regions",
            "tender_amount", "website", "acquisition_source",
            "origin_text", "analytic_result", "release_time",
            "end_time", "path", "create_time", "update_time", "announcement_type"
        ]
    },
    "announcement_zhongbiao": {
        "fields": [
            "id", "task_id", "project_name", "industries", "regions",
            "website", "acquisition_source", "origin_text",
            "analytic_result", "receive_time", "path",
            "create_time", "update_time", "announcement_type"
        ]
    },
    "gov_procurement_info1": {
        "fields": [
            "id", "task_id", "procurement_unit", "project_name", "industries", "regions",
            "announcement_type", "tender_amount", "website", "acquisition_source",
            "release_time", "end_time", "metadata", "origin_text",
            "analytic_result", "path", "create_time", "update_time"
        ]
    },
    "public_resources_info": {
        "fields": [
            "id", "task_id", "project_name", "industries", "regions", "business_type",
            "message_amount", "website", "acquisition_source", "origin_text",
            "analytic_result", "release_time", "end_time", "path",
            "create_time", "update_time"
        ]
    }
}

# ========= 数据库连接 =========
def get_connection():
    return pymysql.connect(
        host='10.0.102.52',
        user='root',
        password='123456',
        database='collection',
        charset='utf8mb4',
        autocommit=False
    )

# ========= 工具函数 =========
def clean_project_name(name):
    name = unescape(name or "")
    name = re.sub(r'<[^>]*>', '', name)
    return name.strip().lower()

def load_last_max_id():
    if os.path.exists(ID_RECORD_FILE):
        with open(ID_RECORD_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip() or DEFAULT_START_ID)
    return DEFAULT_START_ID

def save_new_max_id(new_id):
    with open(ID_RECORD_FILE, "w", encoding="utf-8") as f:
        f.write(str(new_id))

def get_insert_sql(fields):
    field_list = ", ".join(fields)
    placeholder_list = ", ".join([f"%({field})s" for field in fields])
    return f"INSERT INTO {TARGET_TABLE} ({field_list}) VALUES ({placeholder_list})"

# ========= 主逻辑 =========
def main():
    # base_key = next((k for k in TABLE_CONFIG if SOURCE_TABLE.startswith(k)), None)
    base_key = next((k for k in TABLE_CONFIG if SOURCE_TABLE == k), None)
    if base_key is None:
        print(f"未找到数据源 {SOURCE_TABLE} 的字段配置，请检查表名")
        return

    fields = TABLE_CONFIG[base_key]["fields"]
    insert_sql = get_insert_sql(fields)

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    print("加载目标表中的 project_name 去重参考...")
    cursor.execute(f"SELECT project_name FROM {TARGET_TABLE}")
    existing_names = set(
        clean_project_name(row['project_name'])
        for row in cursor.fetchall() if row['project_name']
    )
    print(f"已存在项目名数量：{len(existing_names)}")

    last_max_id = load_last_max_id()
    max_processed_id = last_max_id  # ✅ 初始化，避免未定义
    print(f"上次处理最大 ID：{last_max_id}")

    cursor.execute(f"SELECT MAX(id) AS max_id FROM {TARGET_TABLE}")
    max_id = cursor.fetchone()['max_id'] or 0
    next_id = max_id + 1
    print(f"目标表当前最大 ID：{max_id}")

    last_id = last_max_id
    pbar = tqdm(desc="去重写入", unit="条")

    while True:
        sql = f"""
            SELECT {','.join(fields)} FROM {SOURCE_TABLE}
            WHERE id > %s
            ORDER BY id
            LIMIT %s
        """
        cursor.execute(sql, (last_id, BATCH_SIZE))
        rows = cursor.fetchall()

        if not rows:
            break

        last_id = rows[-1]['id']
        batch_seen = set()
        insert_batch = []

        for row in rows:
            raw_name = row.get('project_name', "") or ""
            cleaned_name = clean_project_name(raw_name)

            if not cleaned_name or cleaned_name in existing_names or cleaned_name in batch_seen:
                continue

            batch_seen.add(cleaned_name)
            row['id'] = next_id
            next_id += 1
            insert_batch.append(row)

            if len(insert_batch) >= INSERT_BATCH_SIZE:
                try:
                    cursor.executemany(insert_sql, insert_batch)
                    conn.commit()
                    existing_names.update(batch_seen)
                    insert_batch.clear()
                    max_processed_id = last_id
                except Exception as e:
                    print(f"批量插入失败: {e}")
                    conn.rollback()

        if insert_batch:
            try:
                cursor.executemany(insert_sql, insert_batch)
                conn.commit()
                existing_names.update(batch_seen)
                max_processed_id = last_id
            except Exception as e:
                print(f"批量插入失败: {e}")
                conn.rollback()

        pbar.update(len(rows))

    pbar.close()
    cursor.close()
    conn.close()
    save_new_max_id(max_processed_id)
    print(f"完成处理，新最大 ID 记录为：{max_processed_id}")

if __name__ == "__main__":
    main()
