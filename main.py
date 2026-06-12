from flask import Flask,render_template,url_for,redirect
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text,ForeignKey
from flask_login import LoginManager,UserMixin,login_user,logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from form import Login,Register

load_dotenv()

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

#Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

#Prepare DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
db.init_app(app)
# Create User_DB
class User(UserMixin,db.Model):
    __tablename__ = "user_info"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    username: Mapped[str] = mapped_column(String,nullable=False)
    email:Mapped[str] = mapped_column(String,nullable=False,unique=True)
    password:Mapped[str] = mapped_column(String,nullable=False)

#Create DB
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/register",methods = ["GET","POST"])
def register():
    register_form = Register()
    if register_form.validate_on_submit():
        new_user = User(
            username = register_form.name.data,
            email = register_form.email.data,
            password = generate_password_hash(password=register_form.password.data,salt_length=8)
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("home"))
    return render_template("register.html",form = register_form)

@app.route("/login")
def login():
    login_form = Login()
    return render_template("login.html",form = login_form)

if __name__ == "__main__":
    app.run(debug=True)