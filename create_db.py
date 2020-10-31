from project import db
from project.database import posts, writer

db.create_all()
db.session.add(writer('ikan','asin'))
db.session.add(posts('First !','First blog'))
db.session.commit()