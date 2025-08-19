import os
import subprocess
import threading
import pymysql

PYTHON_EXECUTABLE = r"D:\PythonProject\.venv\Scripts\python.exe"

# === 配置区 ===
RAW_SOURCE_TABLE = "public_resources_info_new" # 只修改：announcement、announcement_kaibiao
# announcement_pingbiao、announcement_zhongbiao、gov_procurement_info1、public_resources_info_new
TEMP_TABLE = f"temp_{RAW_SOURCE_TABLE}"
DEDUPLICATE_SCRIPT = "deduplicate1.py"

SUB_SCRIPTS = [
    "bid_evaluation_event_bk.py",
    "bid_opening_event_bk.py",
    "bid_publicity_bk.py",
    "bid_result_publicity_bk.py",
    "contract_signing.py",
    "tender_info.py"
]

def run_script(script, env_vars=None):
    print(f"\n[运行] {script}")
    env = os.environ.copy()
    if env_vars:
        env.update(env_vars)
    try:
        subprocess.run([PYTHON_EXECUTABLE, script], env=env, check=True)
        print(f"[完成] {script}")
    except subprocess.CalledProcessError as e:
        print(f"[失败] {script}\n错误信息：{e}")

def truncate_temp_table():
    print(f"\n[清空] 临时表 {TEMP_TABLE}")
    conn = pymysql.connect(
        host='10.0.102.52',
        user='root',
        password='123456',
        database='collection',
        charset='utf8mb4',
        autocommit=True
    )
    with conn.cursor() as cursor:
        cursor.execute(f"TRUNCATE TABLE {TEMP_TABLE}")
    conn.close()
    print("[完成] 临时表清空")

def main():
    # 1. 清空临时表
    truncate_temp_table()

    # 2. 执行 deduplicate.py，将去重数据写入临时表
    run_script(DEDUPLICATE_SCRIPT, {
        "RAW_SOURCE_TABLE": RAW_SOURCE_TABLE,
        "TARGET_TABLE": TEMP_TABLE
    })

    # 3. 并行执行后续子脚本
    threads = []
    for script in SUB_SCRIPTS:
        t = threading.Thread(target=run_script, args=(script, {"SOURCE_TABLE": TEMP_TABLE}))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\n 所有处理完成。")

if __name__ == "__main__":
    main()