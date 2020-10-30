from app import db, bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class posts(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String)
	body = db.Column(db.String)

	def __init__(self,title,body):
		self.title = title
		self.body = body

class writer(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String)
	password = db.Column(db.String)

	def __init__(self,name,password):
		self.name = name
		self.password = bcrypt.generate_password_hash(password).decode('utf-8')