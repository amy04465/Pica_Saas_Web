'''
__data__ = 2017/8/22
__author__ = amy liu
'''
# coding = utf-8

from page_obj.loginPage import LoginPage
from test_case.test_HomePage import HomePageTest

from congif.constant import *
from congif.Mytest import Mytest

class loginTest(Mytest):
    '''
    登录测试用例
    '''

    driver = dr

    @classmethod
    def setUpClass(cls):
        # cls.driver.implicitly_wait(30)
        # cls.driver.maximize_window()
        # cls.driver.verificationErrors = []
        # cls.driver.accept_next_alert = True
        HomePageTest.test_Open_loginWindow(cls)
        print('test case start')

    # testHomePage = HomePageTest()
    # loginPage = LoginPage()

    def test_login(self):
        # 调用 打开登录窗口'test_Open_loginWindow()'
        self.testHomePage.test_Open_loginWindow()
        #HomePageTest.test_Open_loginWindow(self)
        loginPage = LoginPage()
        self.loginPage.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        self.assertTrue(self.loginPage.show_personalImgUrl(), "用户登录失败")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('test case end')




