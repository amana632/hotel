from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='main://username:aman@123/db' + os.path.join(basedir, 'main.db')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from main import route