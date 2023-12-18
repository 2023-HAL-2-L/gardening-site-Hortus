from flask_sqlalchemy import SQLAlchemy
# from __init__ import app

db = SQLAlchemy()

def init_db(app):
  
  db.init_app(app)