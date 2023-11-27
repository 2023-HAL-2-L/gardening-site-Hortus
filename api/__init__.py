from flask import Flask, render_template, request, redirect, url_for, flash
from api.database import db
from api.views.user import user
from api.views.auth import auth
from api.views.shop import shop
from api.views.column import column
from api.views.thread import thread
from api.views.main import main
from flask_login import LoginManager

def create_app():
    
    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)
    login = LoginManager(app)
    app.register_blueprint(main , url_prefix="/")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(shop, url_prefix="/shop")
    app.register_blueprint(column, url_prefix="/column")
    app.register_blueprint(thread, url_prefix="/thread")
    
    return app, login

app,login = create_app()