from flask import Flask, render_template, request
import mysql.connector
from flask_cors import CORS
import json

mysql = mysql.connector.connect(
    user='web',
    password='webPass',
    host='127.0.0.1',
    database='library'
)

app = Flask(__name__)
CORS(app)

@app.route("/books")
def get_books():
    cur = mysql.cursor()
    cur.execute('''SELECT * FROM books''')
    rv = cur.fetchall()
    books = [{'ID': row[0], 'Title': row[1], 'Author': row[2]} for row in rv]
    return json.dumps({'Books': books, 'count': len(books)})

@app.route("/users")
def get_users():
    cur = mysql.cursor()
    cur.execute('''SELECT * FROM users''')
    rv = cur.fetchall()
    users = [{'ID': row[0], 'Name': row[1], 'Email': row[2]} for row in rv]
    return json.dumps({'Users': users, 'count': len(users)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
