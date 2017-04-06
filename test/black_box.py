# -*- coding:utf-8 -*-
from flask_testing import LiveServerTestCase
from utils import BaseTestCase
import json
import unittest


class FlaskTestCase(BaseTestCase):

    def test_black_box_1(self):
        response = self._patch_rifle(36, 41, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_2(self):
        response = self._patch_rifle(1, 41, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_3(self):
        response = self._patch_rifle(0, 41, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_4(self):
        response = self._patch_rifle(69, 41, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_5(self):
        response = self._patch_rifle(70, 41, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_6(self):
        response = self._patch_rifle(-1, 41, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_7(self):
        response = self._patch_rifle(36, 1, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_8(self):
        response = self._patch_rifle(36, 0, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_9(self):
        response = self._patch_rifle(36, 79, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_10(self):
        response = self._patch_rifle(36, 80, 46)
        self.assertEquals(response.status_code, 200)

    def test_black_box_11(self):
        response = self._patch_rifle(36, 41, 1)
        self.assertEquals(response.status_code, 200)

    def test_black_box_12(self):
        response = self._patch_rifle(36, 41, 0)
        self.assertEquals(response.status_code, 200)

    def test_black_box_13(self):
        response = self._patch_rifle(36, 41, 89)
        self.assertEquals(response.status_code, 200)

    def test_black_box_14(self):
        response = self._patch_rifle(36, 41, 90)
        self.assertEquals(response.status_code, 200)

    def test_black_box_15(self):
        response = self._patch_rifle(-2, 41, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_16(self):
        response = self._patch_rifle(71, 41, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_17(self):
        response = self._patch_rifle(36, 81, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_18(self):
        response = self._patch_rifle(36, -1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_19(self):
        response = self._patch_rifle(36, 41, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_20(self):
        response = self._patch_rifle(36, 41, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_21(self):
        response = self._patch_rifle(0, 0, 0)
        self.assertEquals(response.status_code, 417)

if __name__ == '__main__':
    unittest.main()