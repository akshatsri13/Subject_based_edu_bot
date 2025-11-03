import sqlite3

def db_connect():
    conn = sqlite3.connect("subject_bot.db")
    # cursor = conn.cursor()
    conn.execute("""
           CREATE TABLE IF NOT EXISTS subject(
                   id TEXT PRIMARY KEY,
                   user_query TEXT,
                   intent TEXT,
                   bot_response TEXT
    )
""")
    conn.commit()
    return conn

def save_chat(user_query, intent, bot_response):
    conn = db_connect()
    # cursor = conn.cursor()
    conn.execute("INSERT INTO subject(user_query, intent, bot_response) VALUES(?,?,?)",(user_query,intent,bot_response))
    conn.commit()
    conn.close()

def get_history():
    conn = db_connect()
    # cursor = conn.cursor()
    rows = conn.execute("SELECT user_query, intent, bot_response FROM subject").fetchall()
    conn.close()
    return rows    