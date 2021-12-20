from flask import Flask
import os
import psycopg2

# Initiate Flask App
app = Flask(__name__)

# Getting the DB URL from the local environment variable
DATABASE_URL = os.getenv('DATABASE_URL', None)
# Connecting to Postgres DB on Heroku, and set the connection to autocommit
conn = psycopg2.connect(
    DATABASE_URL,
    sslmode='require'
)
conn.set_session(autocommit=True)

# Open a cursor to perform database operations
cur = conn.cursor()

# For first use
try:
    # Create a DB named "users"
    cur.execute("CREATE TABLE users (user_id serial PRIMARY KEY, username VARCHAR ( 50 ) UNIQUE NOT NULL);")
    # Insert a dummy user
    cur.execute("INSERT INTO users (user_id, username) VALUES (1, 'Heroku');")
    # Commit all changes
    conn.commit()
except Exception as e:
    print("Table is already exists...")

BASE_HTML = '''<!DOCTYPE html>
<html>
   <body>
      <h1>Heroku Rules!</h1>
      <img src="http://i.stack.imgur.com/SBv4T.gif" alt="this slowpoke moves"  width="250" />
   </body>

</html>'''


@app.route("/")
def index():
    return BASE_HTML


@app.route("/users")
def users():
    cur.execute("SELECT * FROM users;")
    user = cur.fetchone()
    return f"User ID: {user[0]}\nUser Name: {user[1]}"


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)
