from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class MemoForm(FlaskForm):
	name=StringField('Name', validators=[DataRequired(), Length(1,50)])
	body=TextAreaField('Message', validators=[DataRequired(), Length(1,200)])
	submit=SubmitField()