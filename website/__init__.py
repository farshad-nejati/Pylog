from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.session import Session
# from flask.ext.login import LoginManager

app = Flask(__name__)   # global flask object

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://pylog:pylog@localhost/pylog'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

print("this is init and run successfully")
db = SQLAlchemy(app)

app.secret_key = 'Secret'
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
app.config['SESSION_SQLALCHEMY_TABLE'] = 'sessions'

session = Session(app)
session.app.session_interface.db.create_all()

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'login' #redirection view for login
login_manager.init_app(app)


from website import models
from website import views