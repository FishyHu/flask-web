import unittest

from flask_login import current_user
from base import baseTest

class basicTest(baseTest):
	def test_index(self):
		rv = self.client.get('/login',content_type='html/text')
		self.assertEqual(rv.status_code,200)

	def test_page(self):
		rv = self.client.get('/login')
		self.assertIn(b'Login',rv.data)

	def test_page2(self):
		rv = self.client.get('/register')
		self.assertIn(b'Register',rv.data)

	def test_page3(self):
		rv = self.client.get('/home')
		self.assertIn(b'Oh hi !',rv.data)

	def test_needLogin(self):
		rv = self.client.get('/',follow_redirects=True)
		self.assertIn(b'Please log in',rv.data)

	def test_needLogin2(self):
		rv = self.client.get('/add',follow_redirects=True)
		self.assertIn(b'Please log in',rv.data)

	def test_needLogin3(self):
		rv = self.client.get('/quit',follow_redirects=True)
		self.assertIn(b'Please log in',rv.data)

	def test_needLogin4(self):
		rv = self.client.get('/about',follow_redirects=True)
		self.assertIn(b'Please log in',rv.data)

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

if __name__ == '__main__':
	unittest.main()