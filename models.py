"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL='https://support.plymouth.edu/kb_images/Yammer/default.jpeg'

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        a = self
        return f"<Athlete id={a.id} first_name={a.first_name} last_name={a.last_name}>"

    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    
    first_name = db.Column(db.String(30),
                            nullable=False)
    
    last_name = db.Column(db.String(30),
                            nullable=False)
    
    image_url = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE_URL)




