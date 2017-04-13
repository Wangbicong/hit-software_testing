# -*- coding:utf-8 -*-
import unittest

from utils import BaseTestCase


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

    def test_black_box_22(self):
        response = self._patch_rifle(36, -1, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_23(self):
        response = self._patch_rifle(36, -1, 0)
        self.assertEquals(response.status_code, 400)

    def test_black_box_24(self):
        response = self._patch_rifle(36, -1, 1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_25(self):
        response = self._patch_rifle(36, 0, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_26(self):
        response = self._patch_rifle(36, 1, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_27(self):
        response = self._patch_rifle(36, -1, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_28(self):
        response = self._patch_rifle(36, -1, 90)
        self.assertEquals(response.status_code, 400)

    def test_black_box_29(self):
        response = self._patch_rifle(36, -1, 89)
        self.assertEquals(response.status_code, 400)

    def test_black_box_30(self):
        response = self._patch_rifle(36, 0, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_31(self):
        response = self._patch_rifle(36, 1, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_32(self):
        response = self._patch_rifle(36, 81, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_33(self):
        response = self._patch_rifle(36, 81, 0)
        self.assertEquals(response.status_code, 400)

    def test_black_box_34(self):
        response = self._patch_rifle(36, 81, 1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_35(self):
        response = self._patch_rifle(36, 80, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_36(self):
        response = self._patch_rifle(36, 79, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_37(self):
        response = self._patch_rifle(36, 81, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_38(self):
        response = self._patch_rifle(36, 81, 90)
        self.assertEquals(response.status_code, 400)

    def test_black_box_39(self):
        response = self._patch_rifle(36, 81, 89)
        self.assertEquals(response.status_code, 400)

    def test_black_box_40(self):
        response = self._patch_rifle(36, 80, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_41(self):
        response = self._patch_rifle(36, 79, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_42(self):
        response = self._patch_rifle(-2, -1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_43(self):
        response = self._patch_rifle(-1, -1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_44(self):
        response = self._patch_rifle(0, -1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_45(self):
        response = self._patch_rifle(-2, 0, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_46(self):
        response = self._patch_rifle(-2, 1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_47(self):
        response = self._patch_rifle(71, -1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_48(self):
        response = self._patch_rifle(70, -1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_49(self):
        response = self._patch_rifle(69, -1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_50(self):
        response = self._patch_rifle(71, 0, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_51(self):
        response = self._patch_rifle(71, 1, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_52(self):
        response = self._patch_rifle(-2, 81, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_53(self):
        response = self._patch_rifle(-1, 81, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_54(self):
        response = self._patch_rifle(0, 81, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_55(self):
        response = self._patch_rifle(-2, 80, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_56(self):
        response = self._patch_rifle(-2, 79, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_57(self):
        response = self._patch_rifle(71, 81, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_58(self):
        response = self._patch_rifle(70, 81, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_59(self):
        response = self._patch_rifle(69, 81, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_60(self):
        response = self._patch_rifle(71, 80, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_61(self):
        response = self._patch_rifle(71, 79, 46)
        self.assertEquals(response.status_code, 400)

    def test_black_box_62(self):
        response = self._patch_rifle(-2, 41, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_63(self):
        response = self._patch_rifle(-1, 41, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_64(self):
        response = self._patch_rifle(0, 41, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_65(self):
        response = self._patch_rifle(-2, 41, 0)
        self.assertEquals(response.status_code, 400)

    def test_black_box_66(self):
        response = self._patch_rifle(-2, 41, 1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_67(self):
        response = self._patch_rifle(71, 41, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_68(self):
        response = self._patch_rifle(70, 41, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_69(self):
        response = self._patch_rifle(69, 41, -1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_70(self):
        response = self._patch_rifle(71, 41, 0)
        self.assertEquals(response.status_code, 400)

    def test_black_box_71(self):
        response = self._patch_rifle(71, 41, 1)
        self.assertEquals(response.status_code, 400)

    def test_black_box_72(self):
        response = self._patch_rifle(-2, 41, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_73(self):
        response = self._patch_rifle(-1, 41, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_74(self):
        response = self._patch_rifle(0, 41, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_75(self):
        response = self._patch_rifle(-2, 41, 90)
        self.assertEquals(response.status_code, 400)

    def test_black_box_76(self):
        response = self._patch_rifle(-2, 41, 89)
        self.assertEquals(response.status_code, 400)

    def test_black_box_77(self):
        response = self._patch_rifle(71, 41, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_78(self):
        response = self._patch_rifle(70, 41, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_79(self):
        response = self._patch_rifle(69, 41, 91)
        self.assertEquals(response.status_code, 400)

    def test_black_box_80(self):
        response = self._patch_rifle(71, 41, 90)
        self.assertEquals(response.status_code, 400)

    def test_black_box_81(self):
        response = self._patch_rifle(71, 41, 89)
        self.assertEquals(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
