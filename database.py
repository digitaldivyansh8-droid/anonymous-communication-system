import sqlite3

def init_db():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_message(user_id, message):
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO messages (user_id, message) VALUES (?, ?)",
        (user_id, message)
    )

    conn.commit()
    conn.close()
