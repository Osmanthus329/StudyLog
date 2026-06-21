from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField,TextAreaField,DateField
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

class MyTask(FlaskForm):
    task_name = StringField(name = "task",validators=[DataRequired()])
    deadline = DateField(name = "deadline",validators=[DataRequired()])
    priority = StringField(name = "priority")
    status = StringField(name = "status")
    memo = TextAreaField(name = "memo")
    submit = SubmitField(name = "submit")