from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from api.views.form import ExhibitProductForm
from api.models.models import product, product_image, purchase_history
from api.module import generate_uuid, time_now
from api.database import db
import os

user = Blueprint("user", __name__)

@user.route("/")
@login_required
def index():
  return render_template("user/mypage.html")

@user.route("/exhibit" , methods=["GET", "POST"])
@login_required
def exhibit():
  form = ExhibitProductForm()
  if request.method == "GET":
    return render_template("user/product-listing.html", form=form)
  if request.method == "POST":
    if form.validate_on_submit():
      product_id = generate_uuid()
      file = form.image.data
      file_name = secure_filename(file.filename)
      if file_name.endswith(".jpg"):
        file_name = generate_uuid() + ".jpg"
      elif file_name.endswith(".png"):
        file_name = generate_uuid() + ".png"
      elif file_name.endswith(".jpeg"):
        file_name = generate_uuid() + ".jpeg"
      elif file_name.endswith(".gif"):
        file_name = generate_uuid() + ".gif"
      else:
        flash("画像の形式が正しくありません")
        return render_template("user/product-listing.html", form=form)
      file.save(os.path.join("static/images/product/", file_name))
      productData = product(
        product_id=product_id,
        name=form.name.data,
        price=form.price.data,
        description=form.description.data,
        account_id = current_user.id,
        category_id=form.category.data,
        shipping_days_id= form.shipping_days.data,
        is_barter = form.is_barter.data,
        created_at=time_now(),
        updated_at=time_now(),
      )
      images = product_image(
        product_image_id = generate_uuid(),
        product_id = product_id,
        image=os.path.join("images/product/", file_name),
      )
      db.session.add(images)
      db.session.add(productData)
      db.session.commit()
      flash("商品を出品しました")
      return redirect(url_for("user.index"))
    flash("商品を正しく入力してください")
    return render_template("user/product-listing.html", form=form)


@user.route("/myexhibit")
@login_required
def myexhibit():
  return render_template("user/myexhibit.html")

@user.route("/order")
@login_required
def orders():
  orders = purchase_history.query.filter_by(buy_account_id=current_user.id).all()
  return render_template("user/purchase-history.html", orders = orders)

@user.route("/product")
@login_required
def my_products():
  products = product.query.filter_by(account_id=current_user.id, is_sold = 0).all()
  return render_template("user/my-listing.html", products = products)

# @user.route("/mycolumn")
# @login_required
# def mycolumn():
#   return render_template("user/mycolumn.html")

@user.route("/trade")
@login_required
def trade():
  products = product.query.filter_by(account_id=current_user.id, is_barter = 1).all()
  return render_template("user/Waiting-approval.html")