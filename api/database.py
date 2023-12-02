from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()

def init_db(app, migrate_dir=None):
  db.init_app(app)
  Migrate(app, db, migrate_dir) if migrate_dir else Migrate(app, db)
  # ma.init_app(app)
  # with app.app_context():
  #   db.create_all()
  #   db.session.commit()