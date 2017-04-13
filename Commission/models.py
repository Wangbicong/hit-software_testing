# -*- coding:utf-8 -*-
from passlib.apps import custom_app_context as pwd_context
from Commission import db
from exceptions import *


class Rifle(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    lock = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    barrel = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='rifles')

    def __init__(self, username, lock=0, stock=0, barrel=0):
        user = User.query.filter_by(username=username).first()
        self.user = user
        self.lock = lock
        self.stock = stock
        self.barrel = barrel

    @staticmethod
    def last_rifle(username):
        user = User.query.filter_by(username=username).first()
        return Rifle.query.filter_by(user=user).order_by(Rifle.id.desc()).first()

    @staticmethod
    def update_rifle(username, lock, stock, barrel):

        if not lock and not stock and not barrel:  # 不允许全部为0
            raise ZeroError

        if Rifle.last_rifle(username):
            rifle = Rifle.last_rifle(username)
        else:
            rifle = Rifle.create_rifle(username)

        rifle.lock += lock
        rifle.stock += stock
        rifle.barrel += barrel

        Rifle.__check_status(rifle, min_value=0)
        db_add_commit(rifle)

    @staticmethod
    def create_rifle(username):
        Rifle.__check_status(Rifle.last_rifle(username))
        rifle = Rifle(username)
        db_add_commit(rifle)
        return rifle

    @staticmethod
    def get_rifles(username):
        user = User.query.filter_by(username=username).first()
        total_num = Rifle.query.filter_by(user=user).count()
        return Rifle.query.filter_by(user=user).limit(total_num-1 if total_num else 0).all()

    @staticmethod
    def __check_status(rifle, min_value=1):  # 添加时元素最小值可以部分为0，提交时最小值为1
        if rifle and not(min_value <= rifle.lock <= 70 and min_value <= rifle.stock <= 80 \
                    and min_value <= rifle.barrel <= 90):
            raise OutOfRangeError


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    flag = db.Column(db.SmallInteger, default=0)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = pwd_context.encrypt(password)

    @staticmethod
    def verify_password(username, password):
        user = User.query.filter_by(username=username).first()
        if user:
            return pwd_context.verify(password, user.password_hash)
        else:
            return False

    @staticmethod
    def add_user(username, password):
        if User.query.filter_by(username=username).first():
            return False
        user = User(username=username, password=password)
        db_add_commit(user)
        return True


def db_add_commit(obj):
    db.session.add(obj)
    db.session.commit()