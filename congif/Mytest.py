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
    dr = browser(2)

    def setUp(self, driver = dr):
        # 前置条件
        # 1. 调用浏览器: 1=Google；2=Firefox
        self.driver = driver
        #self.driver = Mytest.getDriver()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        #self.base_url = LOGIN_URL
        self.verificationErrors = []
        self.accept_next_alert = True
        print('test case start')

    def test_zzz_quit(self):
        self.driver.quit()

    def tearDown(self):
         try:
            self.driver.refresh()
            #将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
         except ConnectionRefusedError as e:
             print(e)
         finally:
            self.assertEqual([], self.verificationErrors)
            print('test case end')

    # @classmethod
    # def getDriver(cls):
    #     cls.driver = browser(2)
    #     return cls.driver
