from flask import Flask,render_template,url_for
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
from form import Login

load_dotenv()

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login")
def login():
    login_form = Login()
    return render_template("login.html",form = login_form)

if __name__ == "__main__":
    app.run(debug=True)