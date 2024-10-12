from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Use a parameterized query to avoid SQL injection
        cursor.execute("SELECT flag FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

    except sqlite3.Error as e:
        # If a database error occurs, display the error
        return f"<h1>Database error: {e}</h1>"

    finally:
        # Ensure the connection is always closed
        conn.close()

    # If the credentials are valid, show the flag
    if result:
        return f"<h1>Flag: {result[0]}</h1>"
    else:
        return "<h1>Invalid credentials</h1>"

if __name__ == '__main__':
    app.run(debug=True)
