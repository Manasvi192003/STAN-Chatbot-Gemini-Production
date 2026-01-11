import sqlite3
conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    role TEXT,
    content TEXT
)
""")

conn.commit()

def save_message(user_id, role, content):
    cursor.execute(
        "INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)",
        (user_id, role, content)
    )
    conn.commit()

def get_last_messages(user_id, limit=6):
    cursor.execute(
        """
        SELECT role, content 
        FROM messages 
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (user_id, limit)
    )
    rows = cursor.fetchall()
    return rows[::-1]







