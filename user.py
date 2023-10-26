from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

user = Blueprint("user", __name__)

@user.route("")
def index():
  return render_template("user/index.html")