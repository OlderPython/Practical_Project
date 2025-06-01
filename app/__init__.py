import os
from flask import Flask
from app.extensions import db
from app.routes.book_routes import book_bp


def create_app():
    app = Flask(__name__)
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.py')
    app.config.from_pyfile(config_path)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(book_bp)

    return app