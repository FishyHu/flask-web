import unittest
from app import app, db

class realTest(unittest.TestCase):
	def test_index(self):
		tester = app.test_client()
		response = tester.get('/',content_type='html/text')
		self.assertEqual(response.status_code,200)

	def test_page(self):
		tester = app.test_client()
		response = tester.get('/')
		self.assertIn(b'Bloggy !',response.data)

	def test_data(self):
		tester = app.test_client()

if __name__ == '__main__':
	unittest.main()