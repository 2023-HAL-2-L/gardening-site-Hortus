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

class User(UserMixin, db.Model):
  __tablename__ = "user"
  id = db.Column(UUIDType(binary=False), primary_key=True, default= uuid.uuid4)
  name = db.Column(db.String(63), nullable=False)
  email = db.Column(db.String(63), nullable=False)
  password = db.Column(db.String(63), nullable=False)
  address = db.Column(db.String(255), nullable=False)
  is_operator = db.Column(db.Boolean, nullable=False)
  created_at = db.Column(db.DateTime, default= datetime.datetime.now(tz_jst), nullable=False)
  updated_at = db.Column(db.DateTime, default= datetime.datetime.now(tz_jst), nullable=False)

  def __init__(self, name, email, password, created_at, updated_at):
    self.name = name
    self.email = email
    self.password = password
    self.created_at = created_at
    self.updated_at = updated_at

  def __repr__(self):
    return "<User %r>" % self.name