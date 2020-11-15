import unittest
from base import baseTest
from project import bcrypt
from flask_login import current_user
from project.database import writer

class writerTest(baseTest):
	def test_register(self):
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