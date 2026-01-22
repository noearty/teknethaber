import sqlite3

DB_PATH = "net_haber.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS haberler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        baslik TEXT,
        ozet TEXT,
        link TEXT UNIQUE,
        kaynak TEXT,
        etiket TEXT,
        gonderildi INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    return conn
