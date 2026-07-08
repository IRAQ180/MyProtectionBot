import sqlite3

# الاتصال بقاعدة البيانات
conn = sqlite3.connect("bot_database.db", check_same_thread=False)
cursor = conn.cursor()

# إنشاء الجداول الأساسية (إذا لم تكن موجودة)
cursor.execute("CREATE TABLE IF NOT EXISTS ranks (user_id INTEGER PRIMARY KEY, rank TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS replies (key TEXT PRIMARY KEY, value TEXT)")
conn.commit()

# دالة لجلب الرتبة
def get_rank(user_id):
    cursor.execute("SELECT rank FROM ranks WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else "عضو"

# دوال الردود الجديدة التي تحتاجها
def add_reply(key, value):
    cursor.execute("INSERT OR REPLACE INTO replies (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

def get_reply(key):
    cursor.execute("SELECT value FROM replies WHERE key = ?", (key,))
    result = cursor.fetchone()
    return result[0] if result else None
