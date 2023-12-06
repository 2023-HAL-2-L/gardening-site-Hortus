from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

shop = Blueprint("shop", __name__)

@shop.route("/shop/")
def shop_def():
  # Todo: 名称変更
  return render_template("item-search-result.html")

@shop.route("/shop/", methods=["GET"])
def shop_get():
  if request.method == "GET":
    
    return redirect(url_for("shop.shop"))