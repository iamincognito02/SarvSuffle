from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='a13ade8068b29063b6cc3336'
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login"
login_manager.login_message_category="info"
from flask_market import routes
