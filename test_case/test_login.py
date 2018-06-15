'''
__data__ = 2017/8/22
__author__ = amy liu
'''
# coding = utf-8
from page_obj.loginPage import LoginPage
# from public.Mytest import Mytest
from page_obj.HomePage import HomePage
from test_case.test_HomePage import *


class loginTest(Mytest):
    '''
    登录测试用例
    '''

    login_username = '13166088360'
    login_password = 'aaa111'

    def test_login(self):

        # HomePageTest.test_Open_HomePage(self)
        HomePageTest.test_Open_loginWindow(self)

        # HomePage.goHomePage(self)
        # HomePage.open_loginWindow(self)
        LoginPage.login(self, self.login_username, self.login_password)

        # 断言结果
        self.assertTrue(LoginPage.show_personalImgUrl(self), "用户登录失败")





