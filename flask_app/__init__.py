from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


def create_app():
    from . import models, views
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    models.init_app(app)
    views.init_app(app)

    return app

