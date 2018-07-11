'''
__data__ = 2017/8/22
__author__ = amy liu
'''
# coding = utf-8
from congif.Mytest import Mytest
from page_obj.HomePage import HomePage
from page_obj.loginPage import LoginPage
from congif.constant import *


class loginTest(Mytest):
    '''
    登录测试用例
    '''
    loginPage = LoginPage()
    homePage = HomePage()

    def open_loginDialog(self):
        self.loginPage.open_loginWindow()
        self.assertIn(u'登录', self.loginPage.show_loginDiaTitle())

    def test_login_success(self):

        # self.loginPage.open_loginWindow()
        # self.assertIn(u'登录', self.loginPage.show_loginDiaTitle())
        self.open_loginDialog()
        self.loginPage.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        self.assertTrue(self.loginPage.show_personalImgUrl(), "用户登录失败")







