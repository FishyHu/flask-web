import unittest
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

if __name__ == '__main__':
	unittest.main()