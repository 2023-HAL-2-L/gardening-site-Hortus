from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# import mysql.connector
from api.database import db
from __init__ import app, login

main = Blueprint("main", __name__)




def connect_db():
    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password="P@ssw0rd", db="py23"
    )

    return conn

@main.route("/", methods=["GET"])
def top():
  return render_template("top.html")

@main.route("/login/", methods = ["GET", "POST"])
def login():
  if current_user.is_authenticated:
    return redirect(url_for("main.top"))
  # forms.pyで定義するloginフォームを読み込む
  # Todo: forms.pyを作成する
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember_me.data)
      return redirect(url_for("main.top"))
    else:
      flash("ログインに失敗しました")
  return render_template("login.html")

@main.route("/logout/", methods = ["GET"])
def logout():
  return render_template("logout.html")

@main.route("/top/", methods = ["GET"])
def top():
  return render_template("top.html")





@app.route("/User-Guide/")
def userGuide():
  return render_template("user-guide.html")
@app.route("/inquiry/")
def inquiry():
  return render_template("inquiry.html")