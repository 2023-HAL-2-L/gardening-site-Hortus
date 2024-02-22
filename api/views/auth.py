from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    current_user,
    logout_user,
    login_required,
    login_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from api.models.models import Account
from api.database import db
from api.views.form import RegistrationForm, LoginForm
from api.module import generate_uuid, time_now

# from __init__ import app, login

auth = Blueprint(
    "auth",
    __name__,
)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.top"))
    form = RegistrationForm()
    if request.method == "GET":
        return render_template("auth/registration.html", form=form)

    if request.method == "POST":
        if form.validate_on_submit():
            account_id = generate_uuid()
            hash_password = generate_password_hash(form.password.data, method="sha256")
            time = time_now()
            account = Account(
                id=account_id,
                name=form.name.data,
                email=form.email.data,
                password=hash_password,
                created_at=time,
                updated_at=time,
            )
            db.session.add(account)
            db.session.commit()
            flash("登録が完了しました")
            return redirect(url_for("auth.login"))
        return render_template("auth/registration.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.top"))

    if request.method == "GET":
        form = LoginForm()
        return render_template("auth/login.html", form=form)

    if request.method == "POST":
        # forms.pyで定義するloginフォームを読み込む
        form = LoginForm()

        if form.validate_on_submit():
            account = Account.query.filter_by(
                email=form.email.data
            ).one_or_none()  # .first()
            if account is None or not check_password_hash(
                account.password, form.password.data
            ):
                flash("アカウントが存在しないかemailかpasswordが間違っています。")
                return render_template("auth/login.html", form=form)
            login_user(account, remember=form.is_keep_login.data)
            next_page = request.args.get("next")
            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("main.top")
            return redirect(next_page)
        return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("ログアウトしました。")
    return redirect(url_for("auth.login"))
