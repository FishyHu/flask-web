from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config.from_object(os.environ['SETTINGS'])

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from database import posts

@app.route('/')
def hello():
	data = posts.query.all()
	return render_template('base.html',all=data)

if __name__ == '__main__':
	app.run()