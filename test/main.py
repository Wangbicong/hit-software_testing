# -*- coding:utf-8 -*-
from flask_testing import LiveServerTestCase
from Commission import create_app, db
import json
import requests
import unittest


class FlaskTestCase(LiveServerTestCase):

    def create_app(self):
        app = create_app(config_object='config.TestingConfig')
        return app

    def test_empty_database(self):
        response = self._get_rifles()
        self.assertEquals(response.status_code, 200)    # 连接成功
        self.assertFalse(json.loads(response.content))  # 数据库为空

    def test_once_post(self):
        response = self._post_rifle()
        self.assertEquals(response.status_code, 416)
        self.assertEquals(json.loads(response.content)['message'], 'Out of range.')

    def test_once_patch(self):
        response = self._patch_rifle()
        self.assertEquals(response.status_code, 200)
        self.assertFalse(json.loads(response.content))

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


if __name__ == '__main__':
    unittest.main()