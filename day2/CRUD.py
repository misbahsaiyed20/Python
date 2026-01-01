import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users WHERE id = 2")
user = cursor.fetchall()
print(user)

#update
if user is None:
    print("Error: User with id= 2 not found.")
else:
    cursor.execute("""
    UPDATE users
    SET name = 'rezin', email = 'rezin@gmail.com'
    WHERE id = 2
""")

    conn.commit()
    print("User with id= 2 updated successfully.")


cursor.execute("SELECT * FROM users WHERE id = 2")
print(cursor.fetchall())

cursor.execute("""
    UPDATE users
    SET name = 'lara', email = 'lara@gmail.com'
    WHERE id = 4
""")
conn.commit()
print("User with id= 4 updated successfully.")

#delete
cursor.execute("""
    DELETE FROM users 
    WHERE id = 5
""")
conn.commit()
print("user with id= 5 is successfully")

conn.close()
