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


    def open_dialog(self):
        self.loginPage.open_loginWindow()
        self.assertIn(u'登录', self.loginPage.show_loginDiaTitle())

    def test_login_success(self):

        # self.loginPage.open_loginWindow()
        # self.assertIn(u'登录', self.loginPage.show_loginDiaTitle())
        self.open_dialog()
        self.loginPage.login(LOGIN_USERNAME, LOGIN_PASSWORD)
        self.assertTrue(self.loginPage.show_personalImgUrl(), "用户登录失败")

    def test_resetPwd_errorCode(self):
        self.open_dialog()
        self.loginPage.click_forgotPwdBtn()
        self.assertTrue(self.loginPage.show_resetDiaTitle(), u'未进入[找回密码]弹窗')
        self.loginPage.resetPWD_input(RESET_ERRORCode)
        self.loginPage.resetPWD(RESET_PHONE, RESET_NEWPwd)
        self.assertTrue(self.loginPage.show_confirmDialog())
        self.loginPage.onConfirmBtn()
        self.assertIn(u'验证码已过期', self.loginPage.show_codeError())
        self.homePage.close_loginWindow()

    # def test_resetPwd_success(self):







