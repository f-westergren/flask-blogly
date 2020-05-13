from models import User, db, Post
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
alan = User(first_name='Alan', last_name='Alda')
joel = User(first_name='Joel', last_name='Burton')
jane = User(first_name='Jane', last_name='Smith')

first = Post(title='My first post', content='I have always wanted to blog. Now I blog!', author_id='1')
second = Post(title='My second post', content='I have always wanted to blog. Now I blog even more!!', author_id='1')
dog = Post(title=f'Dog post', content='My dog is the best, he can play fetch!', author_id='3')

# Add new objects to session
db.session.add_all([alan, joel, jane])
db.session.commit()
db.session.add_all([first, second, dog])
db.session.commit()