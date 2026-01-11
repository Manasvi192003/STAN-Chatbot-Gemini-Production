import sqlite3
import os
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "memory.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    text TEXT
)
""")
conn.commit()

model = SentenceTransformer("all-MiniLM-L6-v2")

user_indexes = {}
user_texts = {}

def _init_user(user_id):
    if user_id not in user_indexes:
        user_indexes[user_id] = faiss.IndexFlatL2(384)
        user_texts[user_id] = []

def _load_user_memory(user_id):
    _init_user(user_id)

    cur.execute(
        "SELECT text FROM memory WHERE user_id = ?",
        (user_id,)
    )
    rows = cur.fetchall()

    for (text,) in rows:
        user_texts[user_id].append(text)
        emb = model.encode([text])
        user_indexes[user_id].add(np.array(emb))
# memory.py
# Lightweight deployment-safe memory stub

def store_memory(user_id, text):
    # Memory disabled in hosted demo to reduce RAM usage
    pass

def retrieve_memory(user_id, query, k=3):
    # No long-term memory retrieval in demo
    return []


def clear_user_memory(user_id):
    cur.execute("DELETE FROM memory WHERE user_id = ?", (user_id,))
    conn.commit()

    user_indexes.pop(user_id, None)
    user_texts.pop(user_id, None)

