# DBの接続の設定
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from api.database import db
from sqlalchemy_utils import UUIDType
import uuid
import datetime
# base_dir = os.path.dirname(__file__)

tz_jst = datetime.timezone(datetime.timedelta(hours=9))
# パスワードをハッシュ化
def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# 入力されたパスワードが登録されているパスワードハッシュと一致するかを確認
def check_password(self, password):
        return check_password_hash(self.password_hash, password)
# いらないので方法の保留
# , on_update= db.CASCADE, on_delete= db.CASCADE
class User(UserMixin, db.Model):
  __tablename__ = "user"
  account_id = db.Column(UUIDType(binary=False), primary_key=True, default= uuid.uuid4)
  name = db.Column(db.String(63), nullable=False)
  email = db.Column(db.String(63), nullable=False)
  password = db.Column(db.String(63), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  payment_method_id = db.Column(db.Integer, nullable=False), db.ForeignKey("payment_method.payment_method_id")
  is_operator = db.Column(db.Boolean, nullable=False)
  created_at = db.Column(db.DateTime, default= datetime.datetime.now(tz_jst), nullable=False)
  updated_at = db.Column(db.DateTime, default= datetime.datetime.now(tz_jst), nullable=False)

  # def __init__(self, name, email, password, created_at, updated_at):
  #   self.name = name
  #   self.email = email
  #   self.password = password
  #   self.created_at = created_at
  #   self.updated_at = updated_at

  # def __repr__(self):
    # return "<User %r>" % self.name
    
class PaymentMethod(db.Model):
  __tablename__ = "payment_method"
  payment_method_id = db.Column(db.Integer, primary_key=True)
  payment_method_name = db.Column(db.String(63), nullable=False)
  is_delete = db.Column(db.Boolean, nullable=False, default=False)
  
class category(db.Model):
  __tablename__ = "category"
  category_id = db.Column(db.Integer, primary_key=True)
  category_name = db.Column(db.String(63), nullable=False)
  is_delete = db.Column(db.Boolean, nullable=False, default=False)
  
class condition(db.Model):
  __tablename__ = "condition"
  condition_id = db.Column(db.Integer, primary_key=True)
  condition_name = db.Column(db.String(63), nullable=False)
  is_delete = db.Column(db.Boolean, nullable=False, default=False)
  
class shopping_method(db.Model):
  __tablename__ = "shopping_method"
  shopping_method_id = db.Column(db.Integer, primary_key=True)
  shopping_method_name = db.Column(db.String(63), nullable=False)
  is_delete = db.Column(db.Boolean, nullable=False, default=False)

class shopping_days(db.Model):
  __tablename__ = "shopping_days"
  shopping_days_id = db.Column(db.Integer, primary_key=True)
  shopping_days_name = db.Column(db.String(63), nullable=False)
  is_delete = db.Column(db.Boolean, nullable=False, default=False)

class product(db.Model):
  __tablename__ = "product"
  product_id = db.Column(db.Integer, primary_key=True)
  product_name = db.Column(db.String(63), nullable=False)
  product_description = db.Column(db.String(255), nullable=False)
  product_price = db.Column(db.Integer, nullable=False)
  product_image = db.Column(db.String(255), nullable=False)
  category_id = db.Column(db.Integer, nullable=False), db.ForeignKey("category.category_id")
  condition_id = db.Column(db.Integer, nullable=False), db.ForeignKey("condition.condition_id")
  shopping_method_id = db.Column(db.Integer, nullable=False), db.ForeignKey("shopping_method.shopping_method_id")
  shopping_days_id = db.Column(db.Integer, nullable=False), db.ForeignKey("shopping_days.shopping_days_id")
  is_delete = db.Column(db.Boolean, nullable=False, default=False)
  created_at = db.Column(db.DateTime, default= datetime.datetime.now(tz_jst), nullable=False)
  updated_at = db.Column(db.DateTime, default= datetime.datetime.now(tz_jst), nullable=False)