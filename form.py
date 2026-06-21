from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField,TextAreaField
from wtforms.validators import DataRequired

class Register(FlaskForm):
    name = StringField(name = "user_name",validators=[DataRequired()])
    email = EmailField(name = "email",validators=[DataRequired()])
    password = PasswordField(name = "password",validators=[DataRequired()])
    submit = SubmitField(name = "submit")
    

class Login(FlaskForm):
    email = EmailField(name = "email",validators=[DataRequired()])
    password = PasswordField(name = "password",validators=[DataRequired()])
    submit = SubmitField(name = "submit")

class MySubject(FlaskForm):
    subject_name = StringField(name = "subject",validators=[DataRequired()])
    description = TextAreaField(name = "description")
    submit = SubmitField(name = "submit")