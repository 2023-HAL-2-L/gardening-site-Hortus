from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.models import Account

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def top():
  if current_user.is_authenticated:
    return render_template("main/top.html", name = current_user.name)
  return render_template("main/top.html")

@main.route("/guide")
def userGuide():
  return render_template("main/user-guide.html")
@main.route("/inquiry", methods=["GET", "POST"])
def inquiry():
  return render_template("main/inquiry.html")

@main.route("/notice/1")
def notice1():
  return render_template("main/notice.html")
@main.route("/notice/2")
def notice2():
  return render_template("main/notice2.html")

@main.route("/notice/3")
def notice3():
  return render_template("main/notice3.html")