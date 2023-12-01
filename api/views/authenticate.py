from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    logout_user,
    login_required,
)
from werkzeug.security import generate_password_hash, check_password_hash
# from models.model import Account
from api.database import db

# from __init__ import app, login

auth = Blueprint("auth", __name__)


@auth.route("/signup/", methods=["POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        address = request.form["address"]
        payment_method_id = request.form["payment_method_id"]
        hash_password = generate_password_hash(password, method="sha256")
        account = Account(name, email, hash_password, address, payment_method_id)
        db.session.add(account)
        db.session.commit()
        return redirect(url_for("auth.login"))
    else:
        return redirect("login")


@auth.route("/login/", methods=["POST"])
def login():
    # if current_user.is_authenticated:
    # return redirect(url_for("main.top"))
    # forms.pyで定義するloginフォームを読み込む
    # Todo: forms.pyを作成する
    # form = LoginForm()
    # if form.validate_on_submit():
    #     account = Account.query.filter_by(accountId=form.account_id.data).one_or_none()
    #     if account and check_password_hash(account.password, form.password.data):
    #         login_user(account, remember=form.remember_me.data)
    #         return redirect(url_for("main.top"))
    #     else:
    #         flash("ログインに失敗しました")
    return render_template("login.html")


@auth.route("/logout/", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect("login")
