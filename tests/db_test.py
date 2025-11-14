""" File is dedicated to learning about sqlite3
"""


import sqlite3

# connect to database (creates if doesnt exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# create a table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    email TEXT UNIQUE,
    age INTEGER
  )
''')

# insert data
cursor.execute(("INSERT INTO users (name, email, age) VALUES (?, ?, ?)"),
               ("Alice", "alice@example.com", 30))

# insert multiple rows
users = [
  ("Bob", "bob@example.com", 25),
  ("Charlie", "charlie@example.com", 35)
]
cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users)

# commit changes
conn.commit()

