import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')

# Create a cursor object
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    flag TEXT NOT NULL
)
''')

# Insert a user with the flag
cursor.execute('''
INSERT INTO users (username, password, flag) VALUES (?, ?, ?)
''', ('admin', 'password123', 'CTF{SQL_Injection_Success}'))  # Fixed missing parenthesis

# Commit and close the connection
conn.commit()
conn.close()
