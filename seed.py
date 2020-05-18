from models import User, db, Post, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
PostTag.query.delete()
User.query.delete()
Post.query.delete()
Tag.query.delete()


# Add users
alan = User(first_name='Alan', last_name='Alda')
joel = User(first_name='Joel', last_name='Burton')
jane = User(first_name='Jane', last_name='Smith')

# Add tags
tech = Tag(name='Technology')
politics = Tag(name='Politics')
pets = Tag(name='Pets')
fun = Tag(name='Fun')

db.session.add_all([alan, joel, jane, tech, politics, pets, fun])
db.session.commit()

# Add posts
first = Post(title='My first computer', content='I have always wanted to blog. Now I blog!', author_id=1, 
             tags=[PostTag(tag_id=tech.id), PostTag(tag_id=fun.id)])
second = Post(title='My political post', content='I have always wanted to blog, about politics!!', author_id=1,
              tags=[PostTag(tag_id=politics.id)])
dog = Post(title=f'Dog post', content='My dog is the best, he can play fetch!', author_id=3,
           tags=[PostTag(tag_id=pets.id), 
                 PostTag(tag_id=fun.id)])

db.session.add_all([first, second, dog])
db.session.commit()


# Add post tags



# Add new objects to session
()z