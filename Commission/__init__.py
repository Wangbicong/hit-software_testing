# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_pyfile('../config.py')

    db.init_app(app)

    from Commission.models import Rifle
    db.create_all(app=app)

    from Commission.views import main_bp
    app.register_blueprint(main_bp)

    return app
