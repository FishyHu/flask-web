from app import db

class posts(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String)
	body = db.Column(db.String)

	def __init__(self,title,body):
		self.title = title
		self.body = body