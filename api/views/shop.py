from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.models import product

from api.views.form import ProductSearchForm

shop = Blueprint("shop", __name__)

@shop.route("/", methods=["GET"])
def shop_get():
  form = ProductSearchForm()
  if request.method == "GET":
    products = product.query.all()
    print(products)
    # for produc in products:
      # print(produc.product_name)
    
    return render_template("item-search-result.html", form = form, products = products)
  if request.method == "POST":
    return render_template("item-search-result.html", form = form)
  
@shop.route("/<string:product_id>", methods=["GET"])
def product_detail(product_id):
  if request.method == "GET":
    print(product_id)
    product_data = product.query.filter_by(product_id = product_id).one_or_none()
    print(product_data)
    return render_template("my-listing-detail.html", product_data = product_data)
  if request.method == "POST":
    return render_template("my-listing-detail.html")