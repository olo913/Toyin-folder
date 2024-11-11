import sqlite3

conn = sqlite3.connect("tutorial.db")

# Creat a cursor
cursor = conn.cursor()

# Creat a table
cursor.execute("""CREATE TABLE IF NOT EXISTS user (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER,
               email TEXT unique
               );""")

name = 'Maya'
age = 20
email = 'Maya12@email.com'

# Insert a row of data
# cursor.execute("INSERT INTO user (name, age, email) VALUES ('John', 30, 'john@email.com') ")
# cursor.execute("INSERT INTO user (name, age, email) VALUES ('Toyin', 10, 'Toyin@email.com')")

# Insert a row of data using placeholders
# cursor.execute("INSERT INTO user (name, age, email) VALUES (?, ?, ?)", (name, age, email))
# cursor.execute("INSERT INTO user (name, email) VALUES (?, ?)", (name, email))

# Update a row of data
cursor.execute("UPDATE users SET age = ? WHERE id = ?", (12, 2))
cursor.execute("UPDATE user SET age = NULL WHERE id = 1")

# Delete a row of data
cursor.execute("SELECT * FROM users WHERE email = 'Maya@email.com' ")

# Insert a column of data
cursor.execute("ALTER TABLE users ADD COLUMN gender TEXT")

# Remove a column
cursor.execute("")

# Select all data
cursor.execute("SELECT * FROM user")
rows = (cursor.fetchall())
for row in rows:
    print(row)



# Save (commit) the changes
conn.commit()