from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

diagnosis = Blueprint("diagnosis", __name__)

@diagnosis.route("/", methods=["GET"])
def top():
    return render_template("personal-diagnosis-start.html")

@diagnosis.route("/1", methods=["GET"])
def top():
    return render_template("diagnosis1.html")

@diagnosis.route("/2", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/3", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/4", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/5", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/6", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/7", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/8", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/9", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/10", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/11", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/12", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/13", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/14", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/15", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/16", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/17", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/18", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/19", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/20", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/21", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/22", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/23", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/24", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
@diagnosis.route("/25", methods=["GET"])
def top():
    return render_template("diagnosis1.html")
