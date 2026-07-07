import sqlite3

conn = sqlite3.connect('ranks.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, rank TEXT)')
conn.commit()

def set_rank(user_id, rank):
    cursor.execute('INSERT OR REPLACE INTO users (user_id, rank) VALUES (?, ?)', (user_id, rank))
    conn.commit()

def remove_rank(user_id):
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()

def get_rank(user_id):
    cursor.execute('SELECT rank FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else "عضو"

def get_rank_level(rank):
    levels = {
        "المطور الأساسي": 8, "مطور": 7, "مطور ثانوي": 6, "مالك": 5,
        "منشئ اساسي": 4, "منشئ": 3, "مدير": 2, "مميز": 1, "عضو": 0
    }
    return levels.get(rank, 0)
