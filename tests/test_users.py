import unittest
from base import baseTest
from project import bcrypt
from flask_login import current_user
from project.database import writer

class realTest(baseTest):
	def test_correctLogin(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='orang',password='orang'),
				follow_redirects=True
				)
			self.assertIn(b'Main Page',rv.data)
			self.assertTrue(current_user.is_active())
			self.assertTrue(current_user.is_authenticated())
			self.assertFalse(current_user.is_anonymous())
			self.assertTrue(current_user.name == 'orang')

			rv = self.client.get('/about',follow_redirects=True)
			self.assertIn(b'About Page',rv.data)

	def test_wrongLogin(self):
		rv = self.client.post(
			'/login',
			data=dict(name='orang',password='aja'),
			follow_redirects=True
			)
		self.assertIn(b'Wait a minute. Who are u ?',rv.data)

	def test_logout(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='orang',password='orang'),
				follow_redirects=True
				)
			self.assertIn(b'Main Page',rv.data)

			rv = self.client.get('/quit',follow_redirects=True)
			self.assertIn(b'Bye...',rv.data)

	def test_data(self):
		rv = self.client.post(
			'/login',
			data=dict(name='orang',password='orang'),
			follow_redirects=True
			)
		self.assertIn(b'it was a good game',rv.data)

class writerTest(baseTest):
	def test_correctRegister(self):
		with self.client:
			rv = self.client.post(
				'/register',
				data=dict(name='ikan',password='asin'),
				follow_redirects=True
				)
			self.assertIn(b'Main Page',rv.data)
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

	def test_getId(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='orang',password='orang'),
				follow_redirects=True
				)
			self.assertTrue(current_user.id == 1)

	def test_checkPassword(self):
		user = writer.query.filter_by(name='orang').first()
		self.assertTrue(bcrypt.check_password_hash(user.password,'orang'))

if __name__ == '__main__':
	unittest.main()