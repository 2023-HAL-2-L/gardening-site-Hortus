from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from __init__ import app

db = SQLAlchemy()
migrate = Migrate(app, db)
def init_db(app):
  
  db.init_app(app)
  # ma.init_app(app)
  # with app.app_context():
  #   db.create_all()
  #   db.session.commit()