from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os
from flask.ext.login import LoginManager
#rom flask.ext.openid import OpenID
#from config import basedir


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://action@localhost/action'
from app import views, models

#lm = LoginManager()
#lm.init_app(app)
#oid = OpenID(app, '/tmp')