from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_year = db.Column(db.Integer)

    def as_dict(self):
        return {
            column.name: getattr(self, column.name) 
            for column in self.__table__.columns
        }