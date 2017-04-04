# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_object='config.Config'):

    app = Flask(__name__)

    app.config.from_object(config_object)

    db.init_app(app)

    from Commission.models import Rifle
    db.create_all(app=app)

    from Commission.api import api_bp
    app.register_blueprint(api_bp)

    return app
