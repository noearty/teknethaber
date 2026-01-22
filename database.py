import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "haberler.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS gonderilen_haberler (
            hash TEXT PRIMARY KEY,
            baslik TEXT,
            kaynak TEXT,
            tarih TEXT
        )
    """)
    return conn
