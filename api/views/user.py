from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

user = Blueprint("user", __name__)

@user.route("/")
@login_required
def index():
  return render_template("mypage.html")