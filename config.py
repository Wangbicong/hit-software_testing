# -*- coding:utf-8 -*-
class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/Commission'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
