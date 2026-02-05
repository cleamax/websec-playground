import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    content TEXT
)
""")

cur.execute("DELETE FROM users")
cur.execute("DELETE FROM comments")

cur.execute("INSERT INTO users (username, password, email) VALUES ('alice', 'password123', 'alice@example.com')")
cur.execute("INSERT INTO users (username, password, email) VALUES ('bob', 'password123', 'bob@example.com')")

cur.execute("INSERT INTO comments (user_id, content) VALUES (1, 'Hello world!')")
cur.execute("INSERT INTO comments (user_id, content) VALUES (2, 'Nice app :)')")

conn.commit()
conn.close()
