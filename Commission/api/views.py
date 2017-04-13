# -*- coding:utf-8 -*-
from flask_restful import Resource, reqparse
from Commission.models import Rifle, User
from Commission.api import api
from Commission.api.errors import *
from Commission.exceptions import *

rifle_parser = reqparse.RequestParser()
rifle_parser.add_argument('lock', type=int, required=True, choices=range(0, 71))
rifle_parser.add_argument('stock', type=int, required=True, choices=range(0, 81))
rifle_parser.add_argument('barrel', type=int, required=True, choices=range(0, 91))


class RiflesApi(Resource):

    def get(self, username):
        if not User.is_existed_user(username):
            return make_response(jsonify(message=u'不存在用户'), 404)
        if User.is_super_user(username):
            return jsonify(User.get_all_user_name())
        else:
            return RiflesApi.get_all_rifles(username)

    @staticmethod
    def get_all_rifles(username):
        result = []
        for rifle in Rifle.get_rifles(username):

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
        return result


class RifleApi(Resource):

    def post(self, username):
        if not User.is_existed_user(username):
            return make_response(jsonify(message=u'不存在用户'), 404)
        if User.is_super_user(username):
            return make_response(jsonify(message=u'无权限'), 404)
        try:
            if Rifle.last_rifle(username):
                Rifle.create_rifle(username)
                return jsonify(message='success')
            else:
                return out_of_range()
        except OutOfRangeError:
            return out_of_range()

    def patch(self, username):
        if not User.is_existed_user(username):
            return make_response(jsonify(message=u'不存在用户'), 404)
        if User.is_super_user(username):
            return make_response(jsonify(message=u'无权限'), 404)
        try:
            args = rifle_parser.parse_args()
            Rifle.update_rifle(username, **args)
        except ZeroError:
            return all_is_zero()
        except OutOfRangeError:
            return out_of_range()
        return jsonify(message='success')


api.add_resource(RiflesApi, '/rifles/<username>')
api.add_resource(RifleApi, '/rifle/<username>')
