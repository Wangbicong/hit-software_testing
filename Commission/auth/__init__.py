# -*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Api

auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp, catch_all_404s=True)

from . import views