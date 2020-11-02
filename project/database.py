from project import db, bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class posts(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String)
	body = db.Column(db.String)
	writer_id = db.Column(db.Integer,ForeignKey('writer.id'))

	def __init__(self,title,body,writer_id):
		self.title = title
		self.body = body
		self.writer_id = writer_id

class writer(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String)
	password = db.Column(db.String)
	relation = relationship('posts',backref='author')

	def __init__(self,name,password):
		self.name = name
		self.password = bcrypt.generate_password_hash(password).decode('utf-8')

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id