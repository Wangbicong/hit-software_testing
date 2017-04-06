# -*- coding:utf-8 -*-
from Commission import db
from exceptions import *


class Rifle(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    lock = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    barrel = db.Column(db.Integer, nullable=False)

    def __init__(self, lock=0, stock=0, barrel=0):
        self.lock = lock
        self.stock = stock
        self.barrel = barrel

    @staticmethod
    def last_rifle():
        return Rifle.query.order_by(Rifle.id.desc()).first()

    @staticmethod
    def update_rifle(lock, stock, barrel):

        if not lock and not stock and not barrel:  # 不允许全部为0
            raise ZeroError

        if Rifle.last_rifle():
            rifle = Rifle.last_rifle()
        else:
            rifle = Rifle.create_rifle()

        rifle.lock += lock
        rifle.stock += stock
        rifle.barrel += barrel

        Rifle.__check_status(rifle, min_value=0)
        db_add_commit(rifle)

    @staticmethod
    def create_rifle():
        Rifle.__check_status(Rifle.last_rifle())
        rifle = Rifle()
        db_add_commit(rifle)
        return rifle

    @staticmethod
    def get_rifles():
        total_num = Rifle.query.count()
        return Rifle.query.limit(total_num-1 if total_num else 0).all()

    @staticmethod
    def __check_status(rifle, min_value=1):  # 添加时元素最小值可以部分为0，提交时最小值为1
        if rifle and not(min_value <= rifle.lock <= 70 and min_value <= rifle.stock <= 80 \
                    and min_value <= rifle.barrel <= 90):
            raise OutOfRangeError


def db_add_commit(obj):
    db.session.add(obj)
    db.session.commit()