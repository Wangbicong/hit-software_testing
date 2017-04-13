# -*- coding:utf-8 -*-
from utils import BaseTestCase
import requests
import json


class WhiteBoxTestCase(BaseTestCase):
    def test_server_start(self):
        response = self._get_rifles()
        self.assertEquals(response.status_code, 200)

    def test_error_url(self):
        response = requests.get(self.get_server_url())
        self.assertEquals(response.status_code, 404)

    def test_error_http_method(self):
        response = requests.get(self.get_server_url() + '/rifle')
        self.assertEquals(response.status_code, 405)

    def test_error_arg(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'error': 1
        })
        self.assertEquals(response.status_code, 400)

    def test_lock_arg_1(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'lock': 1
        })
        self.assertEquals(response.status_code, 400)

    def test_lock_arg_2(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'stock': 1
        })
        self.assertEquals(response.status_code, 400)

    def test_lock_arg_3(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'barrel': 1
        })
        self.assertEquals(response.status_code, 400)

    def test_lock_arg_4(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'lock': 1,
            'stock': 1
        })
        self.assertEquals(response.status_code, 400)

    def test_lock_arg_5(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'stock': 1,
            'barrel': 1
        })
        self.assertEquals(response.status_code, 400)

    def test_lock_arg_6(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'lock': 1,
            'barrel': 1
        })
        self.assertEquals(response.status_code, 400)

    def test_more_arg(self):
        response = requests.patch(self.get_server_url() + '/rifle', json={
            'lock': 1,
            'stock': 1,
            'barrel': 1,
            'error': 1
        })
        self.assertEquals(response.status_code, 200)

    def test_post_rifle_illegal(self):
        response = self._post_rifle()
        self.assertEquals(response.status_code, 416)

    def test_post_rifle_legal(self):
        self._patch_rifle(5, 5, 5)
        response = self._post_rifle()
        self.assertEquals(response.status_code, 200)

    def test_get_rifles_empty(self):
        response = self._get_rifles()
        self.assertFalse(json.loads(response.content))

    def test_get_rifles_0to1000(self):
        self._patch_rifle()
        self._post_rifle()
        response = self._get_rifles()
        self.assertEquals(json.loads(response.content),
                          [{u'profit': 10.0, u'lock': 1, u'barrel': 1, u'stock': 1, u'income': 100}])

    def test_get_rifles_1000to1800(self):
        self._patch_rifle(20, 10, 10)
        self._post_rifle()
        response = self._get_rifles()
        self.assertEquals(json.loads(response.content),
                          [{u'barrel': 10, u'income': 1450, u'lock': 20, u'profit': 167.5, u'stock': 10}])

    def test_get_rifles_1800(self):
        self._patch_rifle(30, 30, 30)
        self._post_rifle()
        response = self._get_rifles()
        self.assertEquals(json.loads(response.content),
                          [{u'profit': 460.0, u'lock': 30, u'barrel': 30, u'stock': 30, u'income': 3000}])

    def test_patch_file_illegal(self):
        response = self._patch_rifle(20, 10, 10)
        self.assertEquals(response.status_code, 200)

    def test_patch_file_legal1(self):
        response = self._patch_rifle(0, 0, 0)
        self.assertEquals(response.status_code, 417)

    def test_patch_file_legal2(self):
        response = self._patch_rifle(90, 0, 0)
        self.assertEquals(response.status_code, 400)

    def test_patch_file_legal3(self):
        response = self._patch_rifle('a', 'a', 'a')
        self.assertEquals(response.status_code, 400)

    def test_patch_two_illegal(self):
        self._patch_rifle(10, 10, 10)
        response = self._patch_rifle(65, 65, 65)
        self.assertEquals(response.status_code, 416)

    def test_patch_two_legal(self):
        self._patch_rifle(10, 10, 10)
        response = self._patch_rifle(10, 10, 10)
        self.assertEquals(response.status_code, 200)

    def test_patch_two_legal_2(self):
        self._patch_rifle(30, 30, 30)
        response = self._patch_rifle(10, 10, 10)
        self.assertEquals(response.status_code, 200)
