# DBの接続の設定
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from api.database import db
# base_dir = os.path.dirname(__file__)

# パスワードをハッシュ化
def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# 入力されたパスワードが登録されているパスワードハッシュと一致するかを確認
def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class User(UserMixin, db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(63), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(20), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False)
  updated_at = db.Column(db.DateTime, nullable=False)

  def __init__(self, name, email, password, created_at, updated_at):
    self.name = name
    self.email = email
    self.password = password
    self.created_at = created_at
    self.updated_at = updated_at

  def __repr__(self):
    return "<User %r>" % self.name