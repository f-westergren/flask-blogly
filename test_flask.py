from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserTestCase(TestCase):
	"""Tests for users"""

	def setUp(self):
		User.query.delete()

		user = User(first_name='Folke', last_name='Filbyte', image_url='www.image.com')
		db.session.add(user)
		db.session.commit()

		self.user_id = user.id
		
	def tearDown(self):
		db.session.rollback()
	
	def test_user_list(self):
		with app.test_client() as client:
			resp = client.get('/', follow_redirects=True)
			html = resp.get_data(as_text=True)

			self.assertEqual(resp.status_code, 200)
			self.assertIn('Filbyte', html)

	def test_user_details(self):
		with app.test_client() as client:
			resp = client.get(f'/users/{self.user_id}')
			html = resp.get_data(as_text=True)

			self.assertEqual(resp.status_code, 200)
			self.assertIn('www.image.com', html)
	
	def test_delete_user(self):
		with app.test_client() as client:
			resp = client.post(f'/users/{self.user_id}/delete')
			user = User.query.get(self.user_id)

			self.assertFalse(user)
	
	def test_edit_user_details(self):
		with app.test_client() as client:
			resp = client.post(f'/users/{self.user_id}/edit', 
				data={'first_name': 'Gustav', 'last_name': 'Vasa', 'image_url': 'www.photos.com'})
			
			user = User.query.get(self.user_id)
			self.assertEqual(user.first_name, 'Gustav')
			self.assertEqual(user.last_name, 'Vasa')
			self.assertEqual(user.image_url,'www.photos.com')


    
