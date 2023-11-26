from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from user import user
from shop import shop
from column import column
from thread import thread

app = Flask(__name__)
login = LoginManager(app)
login.login_view = "login"
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(shop, url_prefix="/shop")
app.register_blueprint(column, url_prefix="/column")
app.register_blueprint(thread, url_prefix="/thread")

def connect_db():
    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password="P@ssw0rd", db="py23"
    )

    return conn

@app.route("/", methods=["GET"])
def top():
  return render_template("top.html")

@app.route("/login/", methods = ["GET"])
def login():
  return render_template("login.html")

@app.route("/logout/", methods = ["GET"])
def logout():
  return render_template("logout.html")

@app.route("/top/", methods = ["GET"])
def top():
  return render_template("top.html")





@app.route("/User-Guide/")
def userGuide():
  return render_template("user-guide.html")
@app.route("/inquiry/")
def inquiry():
  return render_template("inquiry.html")