from flask import *
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['SETTINGS'])

db = SQLAlchemy(app)

from database import *

@app.route('/')
def hello():
	data = posts.query.all()
	return render_template('base.html',all=data)

if __name__ == '__main__':
	app.run()