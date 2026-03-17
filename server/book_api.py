from flask import Flask, jsonify

app = Flask(__name__)

# 书籍数据
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "read": True
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "read": True
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "read": False
    }

]


# 获取所有书籍 GET http://127.0.0.1:5000/books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
