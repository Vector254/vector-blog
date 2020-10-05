from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PostForm(FlaskForm):
	title = StringField("title",validators=[Required()])
	post = TextAreaField("pitch",validators=[Required()])
    author = TextAreaField("author",validators=[Required()])
	submit = SubmitField('submit')

class CommentForm(FlaskForm):
	description = TextAreaField('',validators=[Required()])
	submit = SubmitField() 
