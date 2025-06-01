from flask import Blueprint, jsonify
from app.models.book import Book


book_bp = Blueprint('book_bp', __name__)


@book_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.as_dict() for book in books])
