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

@main.route("/top/", methods = ["GET"])
def top():
  return render_template("top.html")

@main.route("/User-Guide/")
def userGuide():
  return render_template("user-guide.html")
@main.route("/inquiry/")
def inquiry():
  return render_template("inquiry.html")