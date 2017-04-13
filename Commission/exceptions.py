# -*- coding:utf-8 -*-
class OutOfRangeError(Exception):

    status_code = 416
    message = 'Out of range'


class ZeroError(Exception):

    status_code = 417
    message = 'All is zero'


class LoginTwiceError(Exception):
    status_code = 405
    message = u'已注册'