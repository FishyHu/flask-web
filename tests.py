from flask_testing import TestCase
from flask_login import current_user
from project import app, db
from project.database import writer, posts
import unittest

class baseTest(TestCase):
	def create_app(self):
		app.config.from_object('config.test')
		return app

	def setUp(self):
		db.create_all()
		db.session.add(writer('dodo','asin'))
		db.session.add(posts('ikan','ikan itu enak',1))
		db.session.commit()

	def tear_down(self):
		db.session.remove()
		db.drop_all()

class basicTest(baseTest):
	def test_index(self):
		rv = self.client.get('/login',content_type='html/text')
		self.assertEqual(rv.status_code,200)

	def test_page(self):
		rv = self.client.get('/login')
		self.assertIn(b'Login Page',rv.data)

	def test_needLogin(self):
		rv = self.client.get('/',follow_redirects=True)
		self.assertIn(b'Please log in to access this page',rv.data)

	def test_needLogin2(self):
		rv = self.client.get('/add',follow_redirects=True)
		self.assertIn(b'Please log in to access this page',rv.data)

	def test_needLogin3(self):
		rv = self.client.get('/quit',follow_redirects=True)
		self.assertIn(b'Please log in to access this page',rv.data)

class realTest(baseTest):
	def test_correctLogin(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='dodo',password='asin'),
				follow_redirects=True
				)
			self.assertIn(b'Main Page',rv.data)
			self.assertTrue(current_user.name == 'dodo')
			self.assertTrue(current_user.is_active())

			rv = self.client.get('/quit',follow_redirects=True)
			self.assertIn(b'Oh hi !',rv.data)

	def test_wrongLogin(self):
		rv = self.client.post(
			'/login',
			data=dict(name='ikan',password='lele'),
			follow_redirects=True
			)
		self.assertIn(b'Wait a minute. Who are u ?',rv.data)

	def test_correctRegister(self):
		with self.client:
			rv = self.client.post(
				'/register',
				data=dict(name='lele',password='belut'),
				follow_redirects=True
				)
			self.assertIn(b'Main Page',rv.data)
			self.assertTrue(current_user.name == 'lele')
			self.assertTrue(current_user.is_active())

			rv = self.client.get('/quit',follow_redirects=True)
			self.assertIn(b'Oh hi !',rv.data)

	def test_wrongRegister(self):
		rv = self.client.post(
			'/register',
			data=dict(name='lele',password=''),
			follow_redirects=True
			)
		self.assertIn(b'Register Page',rv.data)

	def test_addData(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='dodo',password='asin'),
				follow_redirects=True
				)
			self.assertIn(b'ikan',rv.data)
			self.assertTrue(current_user.name == 'dodo')
			self.assertTrue(current_user.is_active())

			rv = self.client.get('/add',follow_redirects=True)
			self.assertIn(b'Add Some Post',rv.data)

			rv = self.client.post(
				'/add',
				data=dict(title='ruci',body='luffys friend'),
				follow_redirects=True
				)
			self.assertIn(b'ruci',rv.data)
			self.assertIn(b'luffys friend',rv.data)

	def test_data(self):
		rv = self.client.post(
			'/login',
			data=dict(name='lele',password='belut'),
			follow_redirects=True
			)
		self.assertIn(b'ruci',rv.data)
		self.assertIn(b'luffys friend',rv.data)
		self.assertIn(b'ikan',rv.data)
		self.assertIn(b'ikan itu enak',rv.data)
		self.assertIn(b'dodo',rv.data)

if __name__ == '__main__':
	unittest.main()