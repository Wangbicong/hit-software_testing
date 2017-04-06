# -*- coding:utf-8 -*-
from Commission.api import api_bp
from Commission.exceptions import *
from flask import jsonify


@api_bp.app_errorhandler(OutOfRangeError)
def out_of_range(error):
    return jsonify(message=error.message), error.status_code


@api_bp.app_errorhandler(ZeroError)
def all_is_zero(error):
    return jsonify(message=error.message), error.status_code


