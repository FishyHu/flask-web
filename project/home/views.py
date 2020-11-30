from flask import Blueprint, flash, \
render_template, redirect, url_for # pragma: no cover
from flask_login import login_required, \
current_user # pragma: no cover
from .forms import Blogform # pragma: no cover
from project import db # pragma: no cover
from project.database import posts, writer # pragma: no cover

home_blueprint = Blueprint(
	'home',__name__,
	template_folder='templates'
	) # pragma: no cover

@home_blueprint.route('/') # pragma: no cover
@login_required
def main():
	all_data = posts.query.all()
	return render_template('main.html',all=all_data)

@home_blueprint.route('/add',methods=['GET','POST']) # pragma: no cover
@login_required # pragma: no cover
def added():
	form = Blogform()
	if form.validate_on_submit():
		post = posts(
			form.title.data,
			form.body.data,
			current_user.id
		)
		db.session.add(post)
		db.session.commit()
		flash('Added')
		return redirect(url_for('home.main'))
	return render_template('add.html',form=form)

@home_blueprint.route('/about') # pragma: no cover
@login_required # pragma: no cover
def about():
	return render_template('about.html')

@home_blueprint.route('/home') # pragma: no cover
def home():
	return render_template('home.html')