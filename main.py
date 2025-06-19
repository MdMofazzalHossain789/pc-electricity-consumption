import sqlite3
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
import threading
from logger import log_power_usage

def fetch_daily_summary():
    conn = sqlite3.connect("db.sqlite")
    c = conn.cursor()
    c.execute("""
        SELECT DATE(timestamp), SUM(wattage)/1000/60
        FROM power_log
        GROUP BY DATE(timestamp)
        ORDER BY DATE(timestamp) DESC
        LIMIT 30
    """)
    rows = c.fetchall()
    conn.close()
    return rows

def show_gui():
    root = tk.Tk()
    root.title("Electricity Usage Tracker")
    root.geometry("500x400")

    tree = ttk.Treeview(root, columns=("Date", "Usage (kWh)"), show='headings')
    tree.heading("Date", text="Date")
    tree.heading("Usage (kWh)", text="Usage (kWh)")
    tree.pack(fill=tk.BOTH, expand=True)

    def refresh_table():
        # Clear old rows
        for item in tree.get_children():
            tree.delete(item)

        # Load new data
        summary = fetch_daily_summary()
        for date, usage in summary:
            tree.insert("", "end", values=(date, f"{usage:.4f}"))

        # Schedule next refresh after 60 seconds
        root.after(60000, refresh_table)  # 60,000 ms = 60 sec

    refresh_table()  # start first refresh immediately
    root.mainloop()

# Start logger in a background thread
threading.Thread(target=log_power_usage, daemon=True).start()

# Show GUI
show_gui()
