# -*- coding:utf-8 -*-
from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api
from Commission.models import Rifle

main_bp = Blueprint('main', __name__)
api = Api(main_bp)


class RiflesApi(Resource):

    def get(self):
        return 'GET'

    def post(self):
        return 'POST'


class RifleApi(Resource):

    def get(self):
        return 'GET'

    def post(self):
        return 'POST'

api.add_resource(RiflesApi, '/rifles')
api.add_resource(RifleApi, '/rifle')