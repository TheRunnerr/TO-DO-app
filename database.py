import sqlite3

def connect():
    return sqlite3.connect("tasks.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS tasks")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT,
        due_date TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()