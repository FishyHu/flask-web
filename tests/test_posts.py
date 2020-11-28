import unittest
from base import baseTest
from project.database import posts

class postsTest(baseTest):
	def test_addPosts(self):
		rv = self.client.post(
			'/login',
			data=dict(name='orang',password='orang'),
			follow_redirects=True
			)
		self.assertIn(b'Main',rv.data)

		rv = self.client.get('/add',follow_redirects=True)
		self.assertIn(b'Add Posts',rv.data)

		rv = self.client.post(
			'/add',
			data=dict(title='Dunno',body='Dunno'),
			follow_redirects=True
			)
		self.assertIn(b'Dunno',rv.data)
		self.assertIn(b'By orang',rv.data)

if __name__ == '__main__':
	unittest.main()