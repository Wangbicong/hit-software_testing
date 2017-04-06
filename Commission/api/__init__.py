# -*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp, catch_all_404s=True)

from . import views
