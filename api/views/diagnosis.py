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
    return render_template("diagnosis/personal-diagnosis-content.html", count = count)





@diagnosis.route("/1", methods=["GET"])
def diagnosis1():
    return render_template("diagnosis/personal-diagnosis-telling-1.html")

@diagnosis.route("/2", methods=["GET"])
def diagnosis2():
    return render_template("diagnosis/personal-diagnosis-telling-2.html")
@diagnosis.route("/3", methods=["GET"])
def diagnosis3():
    return render_template("diagnosis/personal-diagnosis-telling-3.html")
@diagnosis.route("/4", methods=["GET"])
def diagnosis4():
    return render_template("diagnosis/personal-diagnosis-telling-4.html")
@diagnosis.route("/5", methods=["GET"])
def diagnosis5():
    return render_template("diagnosis/personal-diagnosis-telling-5.html")
@diagnosis.route("/6", methods=["GET"])
def diagnosis6():
    return render_template("diagnosis/personal-diagnosis-telling-6.html")
@diagnosis.route("/7", methods=["GET"])
def diagnosis7():
    return render_template("diagnosis/personal-diagnosis-telling-7.html")
@diagnosis.route("/8", methods=["GET"])
def diagnosis8():
    return render_template("diagnosis/personal-diagnosis-telling-8.html")
@diagnosis.route("/9", methods=["GET"])
def diagnosis9():
    return render_template("diagnosis/personal-diagnosis-telling-9.html")
@diagnosis.route("/10", methods=["GET"])
def diagnosis10():
    return render_template("diagnosis/personal-diagnosis-telling-10.html")
@diagnosis.route("/11", methods=["GET"])
def diagnosis11():
    return render_template("diagnosis/personal-diagnosis-telling-11.html")
@diagnosis.route("/12", methods=["GET"])
def diagnosis12():
    return render_template("diagnosis/personal-diagnosis-telling-12.html")
@diagnosis.route("/13", methods=["GET"])
def diagnosis13():
    return render_template("diagnosis/personal-diagnosis-telling-13.html")
@diagnosis.route("/14", methods=["GET"])
def diagnosis14():
    return render_template("diagnosis/personal-diagnosis-telling-14.html")
@diagnosis.route("/15", methods=["GET"])
def diagnosis15():
    return render_template("diagnosis/personal-diagnosis-telling-15.html")
@diagnosis.route("/16", methods=["GET"])
def diagnosis16():
    return render_template("diagnosis/personal-diagnosis-telling-16.html")
@diagnosis.route("/17", methods=["GET"])
def diagnosis17():
    return render_template("diagnosis/personal-diagnosis-telling-17.html")
@diagnosis.route("/18", methods=["GET"])
def diagnosis18():
    return render_template("diagnosis/personal-diagnosis-telling-18.html")
@diagnosis.route("/19", methods=["GET"])
def diagnosis19():
    return render_template("diagnosis/personal-diagnosis-telling-19.html")
@diagnosis.route("/20", methods=["GET"])
def diagnosis20():
    return render_template("diagnosis/personal-diagnosis-telling-20.html")
@diagnosis.route("/21", methods=["GET"])
def diagnosis21():
    return render_template("diagnosis/personal-diagnosis-telling-21.html")
@diagnosis.route("/22", methods=["GET"])
def diagnosis22():
    return render_template("diagnosis/personal-diagnosis-telling-22.html")
@diagnosis.route("/23", methods=["GET"])
def diagnosis23():
    return render_template("diagnosis/personal-diagnosis-telling-23.html")
@diagnosis.route("/24", methods=["GET"])
def diagnosis24():
    return render_template("diagnosis/personal-diagnosis-telling-24.html")
@diagnosis.route("/25", methods=["GET"])
def diagnosis25():
    return render_template("diagnosis/personal-diagnosis-telling-25.html")
@diagnosis.route("/26", methods=["GET"])
def diagnosis26():
    return render_template("diagnosis/personal-diagnosis-telling-26.html")
@diagnosis.route("/27", methods=["GET"])
def diagnosis27():
    return render_template("diagnosis/personal-diagnosis-telling-27.html")
@diagnosis.route("/28", methods=["GET"])
def diagnosis28():
    return render_template("diagnosis/personal-diagnosis-telling-28.html")
@diagnosis.route("/29", methods=["GET"])
def diagnosis29():
    return render_template("diagnosis/personal-diagnosis-telling-29.html")
@diagnosis.route("/30", methods=["GET"])
def diagnosis30():
    return render_template("diagnosis/personal-diagnosis-telling-30.html")
@diagnosis.route("/31", methods=["GET"])
def diagnosis31():
    return render_template("diagnosis/personal-diagnosis-telling-31.html")
@diagnosis.route("/32", methods=["GET"])
def diagnosis32():
    return render_template("diagnosis/personal-diagnosis-telling-32.html")
@diagnosis.route("/33", methods=["GET"])
def diagnosis33():
    return render_template("diagnosis/personal-diagnosis-telling-33.html")
@diagnosis.route("/34", methods=["GET"])
def diagnosis34():
    return render_template("diagnosis/personal-diagnosis-telling-34.html")
@diagnosis.route("/35", methods=["GET"])
def diagnosis35():
    return render_template("diagnosis/personal-diagnosis-telling-35.html")
@diagnosis.route("/36", methods=["GET"])
def diagnosis36():
    return render_template("diagnosis/personal-diagnosis-telling-36.html")
@diagnosis.route("/37", methods=["GET"])
def diagnosis37():
    return render_template("diagnosis/personal-diagnosis-telling-37.html")
@diagnosis.route("/38", methods=["GET"])
def diagnosis38():
    return render_template("diagnosis/personal-diagnosis-telling-38.html")
@diagnosis.route("/39", methods=["GET"])
def diagnosis39():
    return render_template("diagnosis/personal-diagnosis-telling-39.html")
@diagnosis.route("/40", methods=["GET"])
def diagnosis40():
    return render_template("diagnosis/personal-diagnosis-telling-40.html")
@diagnosis.route("/41", methods=["GET"])
def diagnosis41():
    return render_template("diagnosis/personal-diagnosis-telling-41.html")
@diagnosis.route("/42", methods=["GET"])
def diagnosis42():
    return render_template("diagnosis/personal-diagnosis-telling-42.html")
@diagnosis.route("/43", methods=["GET"])
def diagnosis43():
    return render_template("diagnosis/personal-diagnosis-telling-43.html")
@diagnosis.route("/44", methods=["GET"])
def diagnosis44():
    return render_template("diagnosis/personal-diagnosis-telling-44.html")
@diagnosis.route("/45", methods=["GET"])
def diagnosis45():
    return render_template("diagnosis/personal-diagnosis-telling-45.html")
@diagnosis.route("/46", methods=["GET"])
def diagnosis46():
    return render_template("diagnosis/personal-diagnosis-telling-46.html")
@diagnosis.route("/47", methods=["GET"])
def diagnosis47():
    return render_template("diagnosis/personal-diagnosis-telling-47.html")
@diagnosis.route("/48", methods=["GET"])
def diagnosis48():
    return render_template("diagnosis/personal-diagnosis-telling-48.html")


