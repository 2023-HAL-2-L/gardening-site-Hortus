from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from __init__ import app, login

auth = Blueprint("auth", __name__)

@auth.route("/login/", methods = ["GET", "POST"])
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


@auth.route("/logout/", methods = ["GET"])
def logout():
  return render_template("logout.html")