# -*- coding:utf-8 -*-
from utils import BaseTestCase
import requests
import json


class WhiteBoxTestCase(BaseTestCase):
    def test_login_1(self):
        response = self._add_user('wbc', 'wbc')
        self.assertEquals(response.status_code, 200)
        response = self._check_user('wbc', 'wbc')
        self.assertEquals(response.status_code, 200)

    def test_login_2(self):
        response = self._check_user('wbc', 'wbc')
        self.assertEquals(response.status_code, 405)




