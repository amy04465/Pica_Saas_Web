'''
__data__ = 2017/8/22
__author__ = amy liu
'''
# coding = utf-8
from page_obj.LoginPage import LoginPage
from congif.constant import *
from congif.Mytest import Mytest


class loginTest(Mytest):
    '''
    登录测试用例
    '''
    loginPage = LoginPage()

    def test_login(self):
        self.loginPage.open_loginWindow()
        self.assertIn('登录', self.loginPage.get_mixFromTitle())
        self.loginPage.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        self.assertTrue(self.loginPage.show_personalImgUrl(), "用户登录失败")






