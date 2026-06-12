from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    name = StringField(name = "user_name",validators=[DataRequired()])
    email = EmailField(name = "email",validators=[DataRequired()])
    password = PasswordField(name = "password",validators=[DataRequired()])
    submit = SubmitField(name = "submit")