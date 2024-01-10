from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from api.views.form import ExhibitProductForm
from api.models.models import product
from api.module import generate_uuid, time_now
from api.database import db
import os

user = Blueprint("user", __name__)

@user.route("/")
@login_required
def index():
  return render_template("mypage.html")

@user.route("/exhibit/" , methods=["GET", "POST"])
@login_required
def exhibit():
  form = ExhibitProductForm()
  if request.method == "GET":
    return render_template("product-listing.html", form=form)
  if request.method == "POST":
    if form.validate_on_submit():
      product_id = generate_uuid()
      file = form.image.data
      file_name = secure_filename(file.filename) + "_" + str(time_now())
      file.save(os.path.join("static/img/product/", file_name))
      productData = product(
        product_id=product_id,
        name=form.name.data,
        price=form.price.data,
        description=form.description.data,
        category_id=form.category.data,
        shopping_days_id= form.shopping_days.data,
        is_barter = form.is_barter.data,
        created_at=time_now(),
        updated_at=time_now(),
      )
      db.session.add(productData)
      db.session.commit()
      flash("商品を出品しました")
      return redirect(url_for("user.index"))
    return render_template("product-listing.html", form=form)