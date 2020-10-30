from app import db
from database import posts

db.create_all()
db.session.add(posts('First !','First blog'))
db.session.commit()