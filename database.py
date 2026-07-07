import sqlite3

# الاتصال بقاعدة البيانات
conn = sqlite3.connect('ranks.db', check_same_thread=False)
cursor = conn.cursor()

# إنشاء جدول الرتب إذا لم يكن موجوداً
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        rank TEXT
    )
''')
conn.commit()

# دالة رفع الرتبة
def set_rank(user_id, rank):
    cursor.execute('INSERT OR REPLACE INTO users (user_id, rank) VALUES (?, ?)', (user_id, rank))
    conn.commit()

# دالة الحصول على الرتبة
def get_rank(user_id):
    cursor.execute('SELECT rank FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else "عضو"

# دالة تنزيل الرتبة
def remove_rank(user_id):
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()
