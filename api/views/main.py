from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.models import Account

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def top():
  if current_user.is_authenticated:
    return render_template("top.html", name = current_user.name)
  return render_template("main/top.html")

@main.route("/guide")
def userGuide():
  return render_template("main/user-guide.html")
@main.route("/inquiry", methods=["GET", "POST"])
def inquiry():
  return render_template("main/inquiry.html")