import sqlite3

conn = sqlite3.connect("comoany.db")

db = conn.cursor()

db.execute("""CREATE TABLE IF NOT EXISTS employees (
               id INTEGER PRIMARY KEY,
               name VARCHAR(25) NOT NULL,
               position TXT,
               salary REAL
               );""")

name = 'Maya'
position = 'Accountant'
salary = 20000

db.execute("INSERT INTO employees (name, position, salary) VALUES ('Toyin', 'worker', 20000)")
db.execute("INSERT INTO employees(name, position, salary) VALUES ('Tobi', 'manager', 50000)")

db.execute("INSERT INTO employees (name, position, salary) VALUES('shalom', 'cleaner', 10000)")
db.execute("INSERT INTO employees (name, position, salary) VALUES('Abraham', 'IT', 10000)")

db.execute("UPDATE employees SET name = Evanse, position = 'cleaner' WHERE id = 4 ")

db.execute("")



def count_vowel(string):
    count = 0
    for char in string:
        if char in ("a", "e", "i", "o", "U"):
            count += 1
    return count

print (count_vowel("This is a test sentence"))



keys = ["name", "age", "city"]
value = ["Alice", "30", "New York"]

creation = {}
for key, values in zip(keys, value):
    creation[key] = values
print(f"Dictionary: {creation}")


