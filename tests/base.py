from flask_testing import TestCase

from project import app, db
from project.database import posts, writer

class baseTest(TestCase):
	def create_app(self):
		app.config.from_object('config.nice_test')
		return app

	def setUp(self):
		db.create_all()
		db.session.add(writer('orang','orang'))
		db.session.add(posts('GG !','it was a good game',1))
		db.session.commit()

	def tear_down(self):
		db.session.remove()
		db.drop_all()