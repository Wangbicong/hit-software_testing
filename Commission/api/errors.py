# -*- coding:utf-8 -*-
from flask import jsonify, make_response


def out_of_range():
    return make_response(jsonify(message='Out of range'), 416)


def all_is_zero():
    return make_response(jsonify(message='all is zero'), 417)


