from flask import Flask,render_template,url_for,redirect,flash
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text,ForeignKey
from flask_login import LoginManager,UserMixin,login_user,logout_user,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from form import Login,Register,MySubject

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
    subject = relationship("Subject",back_populates="user") 
#Create Subject_DB
class Subject(db.Model):
    __tablename__ = "subject"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("user_info.id"))
    name:Mapped[str] = mapped_column(String,unique=True,nullable=False)
    description:Mapped[str] = mapped_column(Text)
    user = relationship("User",back_populates="subject")

#Create DB
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("base.html",current_user = current_user)

@app.route("/register",methods = ["GET","POST"])
def register():
    register_form = Register()
    if register_form.validate_on_submit():
        exist_user = db.session.execute(db.select(User).where(User.email == register_form.email.data)).scalar() 
        if exist_user:
            flash("This email is already registered. Please login here.", "danger")
            return redirect(url_for("login"))
        new_user = User(
            username = register_form.name.data,
            email = register_form.email.data,
            password = generate_password_hash(password=register_form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("home"))
    return render_template("register.html",form = register_form,current_user = current_user)

@app.route("/login",methods = ["GET","POST"])
def login():
    login_form = Login()
    if login_form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == login_form.email.data)).scalar() 
        if user:
            if check_password_hash(pwhash=user.password,password=login_form.password.data):
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("This is not correct password. Please enter again.","danger")
                return redirect(url_for("login"))
        else:
            flash("This is not correct email. Please enter again.","danger")
            return redirect(url_for("login"))
    return render_template("login.html",form = login_form,current_user = current_user)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/subject")
def subject():
    subjects = db.session.execute(db.select(Subject)).scalars().all()
    return render_template("subject.html",subjects = subjects)

@app.route("/add_subject",methods = ["GET","POST"])
def add_subject():
    if not current_user.is_authenticated:
        flash("You aren't logging. Please login.",category="danger")
        return redirect(url_for("login"))
    subject_form = MySubject()
    if subject_form.validate_on_submit():
        new_subject = Subject(
            user_id = current_user.id,
            name = subject_form.subject_name.data,
            description = subject_form.description.data
        )
        db.session.add(new_subject)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add_subject.html",form = subject_form)

if __name__ == "__main__":
    app.run(debug=True)