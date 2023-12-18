from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    current_user,
    logout_user,
    login_required,
    login_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.models import Account
from api.database import db
from api.views.form import RegistrationForm, LoginForm

# from __init__ import app, login

auth = Blueprint(
    "auth",
    __name__,
)


@auth.route("/signup/")
def signup_def():
    return render_template("registration.html")


@auth.route("/signup/", methods=["POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.top"))
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # check = Account.query.filter_by(email=form.email.data).first()
            # if check.email == form.email.data:
            #     flash("このメールアドレスは既に登録されています。")
            #     return redirect(url_for("auth.signup"), form=form)
            
            hash_password = generate_password_hash(form.password.data, method="sha256")
            account = Account(name=form.name.data, email=form.email.data)
            account.set_password(hash_password)
            db.session.add(account)
            db.session.commit()
            flash("登録が完了しました")
            return redirect(url_for("auth.login"))
        return redirect(url_for("auth.signup"), form=form)


@auth.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template("login.html", form=form)

    if request.method == "POST":
        if current_user.is_authenticated:
            return redirect(url_for("main.top"))
        # forms.pyで定義するloginフォームを読み込む
        form = LoginForm()

        if form.validate_on_submit():
            account = Account.query.filter_by(email=form.email.data).first()#.one_or_none()
            print(account)
            if account is None and not check_password_hash(
                account.password, form.password.data
            ):
                print("アカウントが存在しないかemailかpasswordが間違っています。")
                flash("アカウントが存在しないかemailかpasswordが間違っています。")
                return redirect(url_for("auth.login"), form=form)
            login_user(account, remember=form.is_keep_login.data)
            return redirect(url_for("main.top"))
        return render_template("login.html", form=form)


@auth.route("/logout/", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("ログアウトしました。")
    return redirect("auth.login")
