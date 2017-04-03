# -*- coding:utf-8 -*-
from Commission import db


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
        rifle = Rifle.last_rifle()
        rifle.lock += lock
        rifle.stock += stock
        rifle.barrel += barrel
        db_add_commit(rifle)

    @staticmethod
    def create_rifle():
        rifle = Rifle()
        db_add_commit(rifle)


def db_add_commit(obj):
    db.add(obj)
    db.commit()