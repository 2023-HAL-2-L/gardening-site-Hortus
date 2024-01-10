from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from api.views.form import ProductSearchForm

shop = Blueprint("shop", __name__)

@shop.route("/", methods=["GET"])
def shop_get():
  form = ProductSearchForm()
  if request.method == "GET":
    return render_template("item-search-result.html", form = form)
  if request.method == "POST":
    return render_template("item-search-result.html", form = form)
  
