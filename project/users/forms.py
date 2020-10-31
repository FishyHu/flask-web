from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class Loginform(FlaskForm):
	name = StringField('name',validators=[DataRequired()])
	password = PasswordField('password',validators=[DataRequired()])

class Registerform(FlaskForm):
	name = StringField('name',validators=[DataRequired()])
	password = PasswordField('password',validators=[DataRequired()])