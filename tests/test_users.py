import unittest
from base import baseTest
from project import db, bcrypt
from flask_login import current_user
from project.database import writer

class realTest(baseTest):
	def test_page(self):
		rv = self.client.get('/login')
		self.assertIn(b'Login',rv.data)

	def test_page2(self):
		rv = self.client.get('/register')
		self.assertIn(b'Register',rv.data)

	def test_page3(self):
		rv = self.client.get('/home')
		self.assertIn(b'Oh hi !',rv.data)
		
	def test_correctLogin(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='orang',password='orang'),
				follow_redirects=True
				)
			self.assertIn(b'Main',rv.data)
			self.assertTrue(current_user.is_active())
			self.assertTrue(current_user.is_authenticated())
			self.assertFalse(current_user.is_anonymous())
			self.assertTrue(current_user.name == 'orang')
			self.assertTrue(current_user.id == 1)

			rv = self.client.get('/about',follow_redirects=True)
			self.assertIn(b'About',rv.data)

	def test_wrongLogin(self):
		rv = self.client.post(
			'/login',
			data=dict(name='orang',password='aja'),
			follow_redirects=True
			)
		self.assertIn(b'Wait a minute. Who are u ?',rv.data)

	def test_correctRegister(self):
		with self.client:
			rv = self.client.post(
				'/register',
				data=dict(name='ikan',password='asin'),
				follow_redirects=True
				)
			self.assertIn(b'Main',rv.data)
			self.assertTrue(current_user.name == 'ikan')
			self.assertTrue(current_user.is_authenticated())
			self.assertTrue(current_user.is_active())
			self.assertFalse(current_user.is_anonymous())

	def test_wrongRegister(self):
		rv = self.client.post(
			'/register',
			data=dict(name='dodo',password=''),
			follow_redirects=True
			)
		self.assertIn(b'Register',rv.data)
			
	def test_checkPassword(self):
		user = writer.query.filter_by(name='orang').first()
		self.assertTrue(bcrypt.check_password_hash(user.password,'orang'))

if __name__ == '__main__':
	unittest.main()