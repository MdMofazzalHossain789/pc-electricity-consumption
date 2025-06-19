import psutil
import GPUtil
import time
import sqlite3
from datetime import datetime

CPU_WATTS = 65
GPU_WATTS = 120
BASE_WATTS = 50

def get_gpu_usage():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].load * 100
    except:
        pass
    return 0

def init_db():
    conn = sqlite3.connect("db.sqlite")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS power_log (
            timestamp TEXT,
            wattage REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_power_usage():
    init_db()
    while True:
        cpu = psutil.cpu_percent()
        gpu = get_gpu_usage()
        total_watt = (cpu / 100 * CPU_WATTS) + (gpu / 100 * GPU_WATTS) + BASE_WATTS

        now = datetime.now().isoformat()
        conn = sqlite3.connect("db.sqlite")
        conn.execute("INSERT INTO power_log (timestamp, wattage) VALUES (?, ?)", (now, total_watt))
        conn.commit()
        conn.close()

        time.sleep(60)  # log every 60 seconds
