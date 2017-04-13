# -*- coding:utf-8 -*-
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from Commission.api import api
from Commission.models import User

user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)
user_parser.add_argument('flag', type=int, required=True, choices=range(0, 2))


class UserApi(Resource):

    def post(self):
        args = user_parser.parse_args()
        if args['flag']:
            if User.add_user(username=args['username'], password=args['password']):
                return jsonify(message='success')
            else:
                return make_response(jsonify(message=u'注册失败'), 405)
        else:
            if User.verify_password(username=args['username'], password=args['password']):
                return make_response(jsonify(message=u'验证成功'), 200)
            else:
                return make_response(jsonify(message=u'验证失败'), 405)


api.add_resource(UserApi, '/login')

