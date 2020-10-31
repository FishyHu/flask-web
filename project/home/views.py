from flask import *
from flask_login import login_required
from project.database import posts

home_blueprint = Blueprint(
	'home',__name__,
	template_folder='templates'
	)

@home_blueprint.route('/')
@login_required
def main():
	all_data = posts.query.all()
	return render_template('main.html',data=all_data)

@home_blueprint.route('/home')
def home():
	return render_template('home.html')