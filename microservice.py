from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_books():
    """Load book data from JSON file."""
    with open('books.json', 'r') as file:
        data = json.load(file)
    return data['books']

@app.route('/view-unread-books', methods=['GET'])
def view_unread_books():
    """Return the list of unread books."""
    books = load_books()
    unread_books = [book for book in books if book['read'] == 'N']
    return jsonify(unread_books)

@app.route('/view-unread-books-by-author', methods=['GET'])
def view_unread_books_by_author():
    """Return the list of unread books by a specific author."""
    author = request.args.get('author', '')
    if not author:
        return jsonify({"error": "Author parameter is required."}), 400

    books = load_books()
    unread_books_by_author = [book for book in books if book['read'] == 'N' and book['author'].lower() == author.lower()]
    return jsonify(unread_books_by_author)

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    app.run(port=5000)
    # app.run(debug=True)
    print("Service running on port 5000")
