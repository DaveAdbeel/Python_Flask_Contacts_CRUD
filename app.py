from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DATABASE_CONNECTION_URI, SECRET_KEY
from routes.contacts import Contacts
from utils.db import db

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(Contacts)
