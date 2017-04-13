# -*- coding:utf-8 -*-
from flask_testing import LiveServerTestCase
from Commission import create_app, db
import requests


class BaseTestCase(LiveServerTestCase):

    def create_app(self):
        app = create_app(config_object='config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def _patch_rifle(self, lock=1, stock=1, barrel=1):
        return requests.patch(self.get_server_url() + '/rifle', json={
            'lock': lock,
            'stock': stock,
            'barrel': barrel
        })

    def _post_rifle(self):
        return requests.post(self.get_server_url() + '/rifle')

    def _get_rifles(self):
        return requests.get(self.get_server_url() + '/rifles')

    def _add_user(self, username, password):
        return requests.post(self.get_server_url() + '/login', json={
            'username': username,
            'password': password,
            'flag': 1
        })

    def _check_user(self, username, password):
        return requests.post(self.get_server_url() + '/login', json={
            'username': username,
            'password': password,
            'flag': 0
        })
