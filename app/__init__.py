from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import DevConf, UserConf


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.config.from_object(DevConf)
else:
    app.config.from_object(UserConf)

db = SQLAlchemy(app)