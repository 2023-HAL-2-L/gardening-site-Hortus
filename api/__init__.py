from flask import Flask
from flask_login import LoginManager
from config import Config
from api.database import db
from api.views.user import user
from api.views.shop import shop
from api.views.column import column
from api.views.thread import thread
from api.views.main import main
from api.views.auth import auth

# from database import init_db
# from api import static

def create_app(local_config="config.py"):
    
    app = Flask(__name__, instance_relative_config=True, template_folder="../templates", static_folder="../static", static_url_path="/")
    app.config.from_object(Config)

    # db = SQLAlchemy(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    login = LoginManager()
    login.login_view = "auth.login"
    login.init_app(app)
    
    from api.models.models import Account
    @login.user_loader
    def load_user(account_id):
        return db.query(Account).get(account_id)
    
    
    app.register_blueprint(main , url_prefix="/")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(shop, url_prefix="/shop")
    app.register_blueprint(column, url_prefix="/column")
    app.register_blueprint(thread, url_prefix="/thread")
    
    return app

app = create_app()