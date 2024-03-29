from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.models import Thread

thread = Blueprint("thread", __name__)

@thread.route("/")
def thread_top():
    threads_data = Thread.query.all()
    return render_template("thread/thread.html")

@thread.route("/new" , methods=["GET", "POST"])
@login_required
def thread_new():
    if request.method == "GET":
        
        return render_template("thread/Bulletin-board-posting.html")
    
    if request.method == "POST":
        
        return render_template("thread/Bulletin-board-posting.html")


@thread.route("/<string:thread_id>" , methods=["GET", "POST"])
def thread_page(thread_id):
    if request.method == "GET":
        
        return render_template("thread/bulletin-board-writing.html")
    
    if request.method == "POST":
        
        return render_template("thread/bulletin-board-writing.html")

