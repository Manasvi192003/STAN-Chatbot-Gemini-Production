import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_DB = os.path.join(BASE_DIR, "memory.db")

conn = sqlite3.connect(MEMORY_DB, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    user_id TEXT,
    content TEXT
)
""")
conn.commit()


def store_memory(user_id: str, text: str):
    cursor.execute(
        "INSERT INTO memory (user_id, content) VALUES (?, ?)",
        (user_id, text)
    )
    conn.commit()


def retrieve_memory(user_id: str, query: str):
    cursor.execute(
        "SELECT content FROM memory WHERE user_id = ? ORDER BY rowid DESC LIMIT 5",
        (user_id,)
    )
    rows = cursor.fetchall()
    return [r[0] for r in rows]

