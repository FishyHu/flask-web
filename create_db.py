from app import db
from database import posts, writer

db.create_all()
db.session.add(writer('ikan','asin'))
db.session.add(posts('First !','First blog'))
db.session.commit()