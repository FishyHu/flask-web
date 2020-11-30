import unittest
from base import baseTest
from flask_login import current_user
from project.database import writer

class homeTest(baseTest):
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

	def test_logout(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='orang',password='orang'),
				follow_redirects=True
				)
			self.assertIn(b'Main',rv.data)

			rv = self.client.get('/quit',follow_redirects=True)
			self.assertIn(b'Bye...',rv.data)

	def test_data(self):
		rv = self.client.post(
			'/login',
			data=dict(name='orang',password='orang'),
			follow_redirects=True
			)
		self.assertIn(b'it was a good game',rv.data)

	def test_realPage(self):
		with self.client:
			rv = self.client.post(
				'/login',
				data=dict(name='orang',password='orang'),
				follow_redirects=True
				)
			self.assertIn(b'Main',rv.data)

			rv = self.client.get('/about',follow_redirects=True)
			self.assertIn(b'About',rv.data)

if __name__ == '__main__':
	unittest.main()