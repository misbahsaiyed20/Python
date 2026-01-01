import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    city TEXT
)
""")

cursor.execute("INSERT INTO users VALUES (1, 'Sara', 'sara@gmail.com', 'Ahmedabad')")
cursor.execute("INSERT  INTO users VALUES (2, 'Ayaan', 'ayaan@gmail.com', 'Ahmedabad')")
cursor.execute("INSERT  INTO users VALUES (3, 'Riya', 'riya@gmail.com', 'Surat')")
cursor.execute("INSERT INTO users VALUES (4, 'Annie', 'annie@gmail.com', 'Jaipur')")
cursor.execute("INSERT INTO users VALUES (5, 'Savana', 'savana@gmail.com', 'Ahmedabad')")

conn.commit()
print("Data inserted successfully")
conn.close()
