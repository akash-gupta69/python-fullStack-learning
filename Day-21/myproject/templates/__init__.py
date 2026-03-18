import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__)

app.config['SECRET_kEY'] = "supersecretkey123"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABSE_URI'] = 'salite:///'+os.path,join(basedir)

db = SQLAlchemy(app)

Migrate(app.db)

login_manager.init_app(app)

login_manager.login_view = 'login'