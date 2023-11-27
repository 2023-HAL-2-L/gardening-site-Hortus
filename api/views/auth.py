from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager

from __init__ import app, login

auth = Blueprint("auth", __name__)