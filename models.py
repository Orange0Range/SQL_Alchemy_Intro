"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String(50), nullable = False, unique = False)
    last_name =  db.Column(db.String(50), nullable = False, unique = False)
    image_url =  db.Column(db.String(500), nullable = True, unique = False)

    def __repr__(self):
        e = self
        return f"<User {e.id} {e.first_name} {e.last_name} {e.image_url}>"

class Post(db.Model):
    """Post Model"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(50), nullable = False, unique = False)
    content = db.Column(db.String(1000), nullable = False, unique = False)
    content_at = db.Column(db.DateTime, nullable = False, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    use = db.relationship('User', backref = 'posts')

    def __repr__(self):
        e = self
        return f"<Post {e.id} {e.title} {e.content_at} {e.user_id}>"
