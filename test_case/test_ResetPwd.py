'''
__data__ = 2018/7/11
__author__ = amy liu
'''
from congif.Mytest import Mytest
from congif.dbConnection import getMobileCode
from page_obj.HomePage import HomePage
from page_obj.loginPage import LoginPage
from congif.constant import *


class ResetPwdTest(Mytest):
    loginPage = LoginPage()
    homePage = HomePage()
    mobileCode = getMobileCode("SELECT content FROM `p_mobile_send_log` where mobile = '18016311461' ORDER BY id DESC LIMIT 1 ",
             'pica')
    code = mobileCode.mobileCode

    def go_resetPwdDialog(self):
        self.loginPage.open_loginWindow()
        self.loginPage.click_forgotPwdBtn()
        self.assertTrue(self.loginPage.show_resetDiaTitle(), u'未进入[找回密码]弹窗')

    def test_resetPwd_errorCode(self):
        self.go_resetPwdDialog()
        self.loginPage.resetPWD_input(RESET_ERRORCode)
        self.loginPage.resetPWD(RESET_PHONE, RESET_NEWPwd)
        self.assertTrue(self.loginPage.show_confirmDialog())
        self.loginPage.onConfirmBtn()
        self.assertIn(u'验证码已过期', self.loginPage.show_codeError())
        self.homePage.close_loginWindow()

    def test_resetPwd_success(self):
        self.go_resetPwdDialog()
        self.loginPage.resetPWD_clickCodeBtn()
        self.loginPage.resetPWD_input(mobileCode.mobileCode)
        self.loginPage.resetPWD(RESET_PHONE, RESET_NEWPwd)
        self.assertTrue(self.loginPage.show_confirmDialog())
        self.loginPage.onConfirmBtn()
        self.homePage.close_loginWindow()

