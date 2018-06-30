'''
__data__ = 2017/11/17
__author__ = amy liu
'''
# coding = utf-8

import unittest
from congif.browserDriver import browser
from congif.constant import *


# setUp() 和 tearDown() 为公共方法，分别作用与每个测试用例的开始和结束，可将其封装起来
class Mytest(unittest.TestCase):
    driver = browser(1)

    def setUp(self):
        # 前置条件
        # 1. 调用浏览器: 1=Google；2=Firefox
        # self.driver = browser(1)
        self.driver = Mytest.getDriver()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = LOGIN_URL
        self.verificationErrors = []
        self.accept_next_alert = True
        print('test case start')

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print('test case end')

    @classmethod
    def getDriver(cls):
        if cls.driver == None:
            cls.driver = browser(1)
        return cls.driver
