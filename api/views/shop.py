from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.models import Account, product, purchase_history
from api.database import db
from api.module import generate_uuid, time_now
from api.views.form import ProductSearchForm

shop = Blueprint("shop", __name__)


@shop.route("/", methods=["GET"])
def shop_get():
    form = ProductSearchForm()
    if request.method == "GET":
        products = product.query.filter_by(is_sold = 0).all()
        print(products)
        # for produc in products:
        # print(produc.product_name)

        return render_template("item-search-result.html", form=form, products=products)
    if request.method == "POST":
        return render_template("item-search-result.html", form=form)


@shop.route("/<string:product_id>", methods=["GET"])
def product_detail(product_id):
    if request.method == "GET":
        product_data = product.query.filter_by(product_id=product_id).one_or_none()
        buy_user = Account.query.filter_by(id=product_data.account_id).one_or_none()
        return render_template(
            "my-listing-detail.html", product_data=product_data, buy_user=buy_user
        )


@shop.route("/<string:product_id>/payment", methods=["GET"])
@login_required
def product_payment(product_id):
    if request.method == "GET":
        product_data = product.query.filter_by(product_id=product_id).one_or_none()
        buy_user = Account.query.filter_by(id=product_data.account_id).one_or_none()
        return render_template(
            "payment.html", product_data=product_data, buy_user=buy_user, product_id=product_id
        )


@shop.route("/<string:product_id>/payment/complete", methods=["GET", "POST"])
@login_required
def product_buy_complete(product_id):
    if request.method == "GET":
        product_data = product.query.filter_by(product_id=product_id).one_or_none()
        buy_user = Account.query.filter_by(id=product_data.account_id).one_or_none()
        product_data.is_sold = True
        # 購入履歴を追加
        purchase_history_data = purchase_history(
            purchase_history_id=generate_uuid(),
            buy_account_id=current_user.id,
            sell_account_id=buy_user.id,
            product_id=product_id,
            created_at=time_now(),
        )
        db.session.add(purchase_history_data)
        db.session.commit()
        return render_template(
            "payment-completed.html", product_data=product_data, buy_user=buy_user
        )
    if request.method == "POST":
        product_data = product.query.filter_by(product_id=product_id).one_or_none()
        buy_user = Account.query.filter_by(id=product_data.account_id).one_or_none()
        product_data.is_sold = True
        # 購入履歴を追加
        purchase_history_data = purchase_history(
            purchase_history_id=generate_uuid(),
            buy_account_id=current_user.id,
            sell_account_id=buy_user.id,
            product_id=product_id,
            created_at=time_now(),
        )
        db.session.add(purchase_history_data)
        db.session.commit()
        return render_template(
            "payment-completed.html", product_data=product_data, buy_user=buy_user
        )
@shop.route("/<string:product_id>/trade", methods=["GET", "POST"])
@login_required
def product_trade(product_id):
    if request.method == "GET":
        product_data = product.query.filter_by(product_id=product_id).one_or_none()
        buy_user = Account.query.filter_by(id=product_data.account_id).one_or_none()
        return render_template(
            "trade.html", product_data=product_data, buy_user=buy_user, product_id=product_id
        )
        
@shop.route("/<string:product_id>/trade/complete", methods=["GET"])
@login_required
def product_trade_complete(product_id):
    if request.method == "GET":
        product_data = product.query.filter_by(product_id=product_id).one_or_none()
        buy_user = Account.query.filter_by(id=product_data.account_id).one_or_none()
        product_data.is_sold = True
        # 購入履歴を追加
        purchase_history_data = purchase_history(
            purchase_history_id=generate_uuid(),
            buy_account_id=current_user.id,
            sell_account_id=buy_user.id,
            product_id=product_id,
            created_at=time_now(),
        )
        db.session.add(purchase_history_data)
        db.session.commit()
        return render_template(
            "trade-completed.html", product_data=product_data, buy_user=buy_user
        )