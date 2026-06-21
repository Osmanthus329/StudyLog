from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField,TextAreaField,DateField,SelectField
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
    subject_name = SelectField(name = "subject",coerce=int)
    deadline = DateField(name = "deadline",validators=[DataRequired()])
    priority = SelectField(name = "priority",choices=["⭐","⭐⭐","⭐⭐⭐"])
    status = SelectField(name = "status",choices = ["未着手","進行中","完了"])
    memo = TextAreaField(name = "memo")
    submit = SubmitField(name = "submit")