from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

thread = Blueprint("thread", __name__)

@thread.route("/")
def thread_top():
    return render_template("thread-top.html")

@thread.route("/new" , methods=["GET", "POST"])
@login_required
def thread_new():
    if request.method == "GET":
        
        return render_template("Bulletin-board-posting.html")
    
    if request.method == "POST":
        
        return render_template("Bulletin-board-posting.html")


@thread.route("/<string:thread_id>" , methods=["GET", "POST"])
def thread_page():
    if request.method == "GET":
        
        return render_template("bulletin-board-writing.html")
    
    if request.method == "POST":
        
        return render_template("bulletin-board-writing.html")

