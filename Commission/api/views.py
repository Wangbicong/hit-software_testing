# -*- coding:utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from Commission.models import Rifle
from Commission.api import api
from Commission.exceptions import *

rifle_parser = reqparse.RequestParser()
rifle_parser.add_argument('lock', type=int, required=True, choices=range(0, 71))
rifle_parser.add_argument('stock', type=int, required=True, choices=range(0, 81))
rifle_parser.add_argument('barrel', type=int, required=True, choices=range(0, 91))


class RiflesApi(Resource):

    def get(self):
        result = []
        for rifle in Rifle.get_rifles():

            income = rifle.lock*45+rifle.stock*30+rifle.barrel*25
            if income <= 1000:
                profit = income * 0.1
            elif income <= 1800:
                profit = 100 + (income-1000)*0.15
            else:
                profit = 220 + (income-1800)*0.2

            result.append({
                'lock': rifle.lock,
                'stock': rifle.stock,
                'barrel': rifle.barrel,
                'income': income,
                'profit': profit,
            })
        return jsonify(result)


class RifleApi(Resource):

    def post(self):
        if Rifle.last_rifle():
            Rifle.create_rifle()
            return jsonify(message='success')
        else:
            return jsonify(message='Out of range'), 416

    def patch(self):
        args = rifle_parser.parse_args()
        Rifle.update_rifle(**args)
        return jsonify(message='success')


api.add_resource(RiflesApi, '/rifles')
api.add_resource(RifleApi, '/rifle')
