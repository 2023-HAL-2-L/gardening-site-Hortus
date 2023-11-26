# DBの接続の設定
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.dirname(__file__)
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "py23.db")