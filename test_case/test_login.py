'''
__data__ = 2017/8/22
__author__ = amy liu
'''
# coding = utf-8
from congif.Mytest import Mytest
from page_obj.LoginPage import LoginPage
from test_case.test_HomePage import *
from congif.constant import *


class loginTest(Mytest):
    '''
    登录测试用例
    '''

    def test_login(self):
        # 调用 打开登录窗口'test_Open_loginWindow()'
        homePageTest = HomePageTest()
        homePageTest.test_Open_loginWindow()

        loginPage = LoginPage()
        loginPage.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        self.assertTrue(loginPage.show_personalImgUrl(), "用户登录失败")






