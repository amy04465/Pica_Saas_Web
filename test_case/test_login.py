'''
__data__ = 2017/8/22
__author__ = amy liu
'''
# coding = utf-8
from congif.Mytest import Mytest
from page_obj.loginPage import LoginPage
from test_case.test_HomePage import *
from congif.constant import *


class loginTest(Mytest):
    '''
    登录测试用例
    '''

    # login_username = '13166088360'
    # login_password = 'aaa111'
    # loginPage = LoginPage.login(LOGIN_USERNAME, LOGIN_PASSWORD)
    def test_login(self):
        # 调用 打开登录窗口'test_Open_loginWindow()'
        homePageTest = HomePageTest()
        homePageTest.test_Open_loginWindow()

        loginPage = LoginPage()
        loginPage.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        self.assertTrue(LoginPage.show_personalImgUrl(self), "用户登录失败")



        # HomePageTest.test_Open_loginWindow(self)
        # LoginPage.login(self, self.login_username, self.login_password)

        # 断言结果
        #self.assertTrue(LoginPage.show_personalImgUrl(self), "用户登录失败")





