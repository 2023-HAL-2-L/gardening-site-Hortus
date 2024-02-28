from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

diagnosis = Blueprint("diagnosis", __name__)

@diagnosis.route("/", methods=["GET"])
def top():
    return render_template("diagnosis/personal-diagnosis-start.html")

@diagnosis.route("/q/1")
def question1():
    return render_template("diagnosis/personal-diagnosis-content.html")

@diagnosis.route("/q/2/<int:count>")
def question2(count):
    return render_template("diagnosis/personal-diagnosis-content-2.html", count = count)

@diagnosis.route("/q/3/<int:count>")
def question3(count):
    return render_template("diagnosis/personal-diagnosis-content-3.html", count = count)

@diagnosis.route("/q/4/<int:count>")
def question4(count):
    return render_template("diagnosis/personal-diagnosis-content-4.html", count = count)

@diagnosis.route("/q/5/<int:count>")
def question5(count):
    return render_template("diagnosis/personal-diagnosis-content-5.html", count = count)





@diagnosis.route("/answer/<int:count>", methods=["GET"])
def answer(count):
    if count == 1:
        return render_template("diagnosis/personal-diagnosis-telling-1.html")
    elif count == 2:
        return render_template("diagnosis/personal-diagnosis-telling-2.html")
    elif count == 3:
        return render_template("diagnosis/personal-diagnosis-telling-3.html")
    elif count == 4:
        return render_template("diagnosis/personal-diagnosis-telling-4.html")
    elif count == 5:
        return render_template("diagnosis/personal-diagnosis-telling-5.html")
    elif count == 6:
        return render_template("diagnosis/personal-diagnosis-telling-6.html")
    elif count == 7:
        return render_template("diagnosis/personal-diagnosis-telling-7.html")
    elif count == 8:
        return render_template("diagnosis/personal-diagnosis-telling-8.html")
    elif count == 9:
        return render_template("diagnosis/personal-diagnosis-telling-9.html")
    elif count == 10:
        return render_template("diagnosis/personal-diagnosis-telling-10.html")
    elif count == 11:
        return render_template("diagnosis/personal-diagnosis-telling-11.html")
    elif count == 12:
        return render_template("diagnosis/personal-diagnosis-telling-12.html")
    elif count == 13:
        return render_template("diagnosis/personal-diagnosis-telling-13.html")
    elif count == 14:
        return render_template("diagnosis/personal-diagnosis-telling-14.html")
    elif count == 15:
        return render_template("diagnosis/personal-diagnosis-telling-15.html")
    elif count == 16:
        return render_template("diagnosis/personal-diagnosis-telling-16.html")
    elif count == 17:
        return render_template("diagnosis/personal-diagnosis-telling-17.html")
    elif count == 18:
        return render_template("diagnosis/personal-diagnosis-telling-18.html")
    elif count == 19:
        return render_template("diagnosis/personal-diagnosis-telling-19.html")
    elif count == 20:
        return render_template("diagnosis/personal-diagnosis-telling-20.html")
    elif count == 21:
        return render_template("diagnosis/personal-diagnosis-telling-21.html")
    elif count == 22:
        return render_template("diagnosis/personal-diagnosis-telling-22.html")
    elif count == 23:
        return render_template("diagnosis/personal-diagnosis-telling-23.html")
    elif count == 24:
        return render_template("diagnosis/personal-diagnosis-telling-24.html")
    elif count == 25:
        return render_template("diagnosis/personal-diagnosis-telling-25.html")
    elif count == 26:
        return render_template("diagnosis/personal-diagnosis-telling-26.html")
    elif count == 27:
        return render_template("diagnosis/personal-diagnosis-telling-27.html")
    elif count == 28:
        return render_template("diagnosis/personal-diagnosis-telling-28.html")
    elif count == 29:
        return render_template("diagnosis/personal-diagnosis-telling-29.html")
    elif count == 30:
        return render_template("diagnosis/personal-diagnosis-telling-30.html")
    elif count == 31:
        return render_template("diagnosis/personal-diagnosis-telling-31.html")
    elif count == 32:
        return render_template("diagnosis/personal-diagnosis-telling-32.html")
    elif count == 33:
        return render_template("diagnosis/personal-diagnosis-telling-33.html")
    elif count == 34:
        return render_template("diagnosis/personal-diagnosis-telling-34.html")
    elif count == 35:
        return render_template("diagnosis/personal-diagnosis-telling-35.html")
    elif count == 36:
        return render_template("diagnosis/personal-diagnosis-telling-36.html")
    elif count == 37:
        return render_template("diagnosis/personal-diagnosis-telling-37.html")
    elif count == 38:
        return render_template("diagnosis/personal-diagnosis-telling-38.html")
    elif count == 39:
        return render_template("diagnosis/personal-diagnosis-telling-39.html")
    elif count == 40:
        return render_template("diagnosis/personal-diagnosis-telling-40.html")
    elif count == 41:
        return render_template("diagnosis/personal-diagnosis-telling-41.html")
    elif count == 42:
        return render_template("diagnosis/personal-diagnosis-telling-42.html")
    elif count == 43:
        return render_template("diagnosis/personal-diagnosis-telling-43.html")
    elif count == 44:
        return render_template("diagnosis/personal-diagnosis-telling-44.html")
    elif count == 45:
        return render_template("diagnosis/personal-diagnosis-telling-45.html")
    elif count == 46:
        return render_template("diagnosis/personal-diagnosis-telling-46.html")
    elif count == 47:
        return render_template("diagnosis/personal-diagnosis-telling-47.html")
    elif count == 48:
        return render_template("diagnosis/personal-diagnosis-telling-48.html")