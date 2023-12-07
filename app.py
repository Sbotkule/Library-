from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/library'
mongo = PyMongo(app)

@app.route("/")
def get_books():
    books = mongo.db.books.find()
    book_list = [{"title": book["title"], "author": book["author"]} for book in books]
    return jsonify({"books": book_list})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
