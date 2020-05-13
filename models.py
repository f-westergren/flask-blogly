"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

DEFAULT_IMAGE_URL='https://support.plymouth.edu/kb_images/Yammer/default.jpeg'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE_URL)

    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name}>"
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'    


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    author = db.relationship('User', backref='posts')

    def __repr__(self):
        p = self
        return f"<Post id={p.id} title={p.title} created_at={p.created_at} author_id={p.author_id}>"
    

def connect_db(app):
    db.app = app
    db.init_app(app)