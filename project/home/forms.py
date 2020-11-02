from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class Blogform(FlaskForm):
	title = StringField('title',validators=[DataRequired()])
	body = TextAreaField('body',validators=[DataRequired()])