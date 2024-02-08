from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


column = Blueprint("column", __name__)

@column.route("/")
def column_top():
    return render_template("column.html")

@column.route("/new" , methods=["GET", "POST"])
@login_required
def new():
    if request.method == "GET":
        
        return render_template("column.html")
    
    if request.method == "POST":
        
        return render_template("column.html")

@column.route("/<string:column_id>" , methods=["GET", "POST"])
def column_page():
    if request.method == "GET":
        
        return render_template("column-detail.html")
    
    if request.method == "POST":
        
        return render_template("column-detail.html")

@column.route("/<string:column_id>/edit" , methods=["GET", "POST"])
@login_required
def column_edit():
    if request.method == "GET":
        
        return render_template("column-edit.html")
    
    if request.method == "POST":
        
        return render_template("column-edit.html")