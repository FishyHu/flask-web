from flask import *
from project import db, bcrypt
from .forms import Loginform, Registerform
from flask_login import login_user, logout_user, login_required
from project.database import writer

users_blueprint = Blueprint(
	'users',__name__,
	template_folder='templates'
	)

@users_blueprint.route('/login',methods=['GET','POST'])
def login():
	form = Loginform()
	if form.validate_on_submit():
		name2 = request.form['name']
		user = writer.query.filter_by(name=name2).first()
		if user is not None and bcrypt.check_password_hash(
			user.password, request.form['password']):
			login_user(user)
			flash('Hi !')
			return redirect(url_for('home.main'))
		else:
			fllash('Wait a minute. Who are u ?')
	return render_template('login.html',form=form)

@users_blueprint.route('/register')
def register():
	form = Registerform()
	if form.validate_on_submit():
		user = writer(
			form.name.data,
			form.password.data
			)
		db.session.add(user)
		db.session.commit()
		flash('Hi there !')
		return redirect(url_for('home.main'))
	return render_template('register.html',form=form)

@users_blueprint.route('/quit')
@login_required
def quit():
	logout_user()
	flash('Bye...')
	return redirect(url_for('home.home'))