"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL='https://support.plymouth.edu/kb_images/Yammer/default.jpeg'

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    def __init__(self, first_name, last_name, image_url=DEFAULT_IMAGE_URL):
        self.first_name = first_name
        self.last_name = last_name
        self.image_url = image_url
        self.full_name = f'{self.first_name} {self.last_name}'
        
        print(self.first_name, self.last_name)

    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name}>"
    
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE_URL)




