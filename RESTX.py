from flask import Flask, request, jsonify
from flask_restx import Resource, Api

app = Flask(__name__)

api = Api(app)
book_ns = api.namespace('')

books = {
    1:{
        "name": "Harry Potter",
        "year": 2000,
        "author": "Joan Routing"
    },
    2: {
        "name": "Le Comte de Monte-Cristo",
        "year": 1844,
        "author": "Alexandre Dumas"
    }
}


@book_ns.route('/books')
class BooksView(Resource):
    def get(self):
        return books, 200

    def post(self):
        req_json = request.json
        books[len(books) + 1] = req_json
        return "", 201

@book_ns.route('/books/<int:bid>')
class BookView(Resource):
    def get(self, bid):
        return books[bid], 200

    def delete(self, bid):
        del books[bid]
        return "", 204

if __name__ == '__main__':
    app.run(debug=False)
