import sqlite3
from datetime import datetime

DB_NAME = "products.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT,
            price TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_product(title, url, price):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO products (title, url, price, date) VALUES (?, ?, ?, ?)",
                (title, url, price, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM products ORDER BY date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows
