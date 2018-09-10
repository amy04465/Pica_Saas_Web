'''
__data__ = 2017/8/22
__author__ = amy liu
'''

# coding = utf-8

import time

from selenium.webdriver.common.by import By
from congif.base import BasePage


class LoginPage(BasePage):
    # 元素维护
    # 登录
    loginBtn_loc = (By.XPATH, '//*[@id="login"]/li[1]/span')
    loginDia_loc = (By.XPATH, '//div[@class="modal-title"]')
    username_loc = (By.XPATH, '//form[@name="mixForm"]/div/input[1]')
    password_loc = (By.XPATH, '//form[@name="mixForm"]/div[3]/input[1]')
    submitBtn_loc = (By.XPATH, '//form[@name="mixForm"]/div[6]/button[1]')
    personalImgUrl_loc = (By.XPATH, '//*[@id="personalImgUrl"]')
    showPhoneError_loc = (By.XPATH, '//form[@name="mixForm"]/div[1]/span[2]')
    showPwdError_loc = (By.XPATH, '//form[@name="mixForm"]/div[3]/span[4]')
    # 注册
    registerBtn_loc = (By.XPATH, './/a[text() = u"注册"]')
    # 忘记密码
    forgotPwdBtn_loc = (By.XPATH, '//form[@name="mixForm"]/div[5]/a')
    reDia_loc = (By.XPATH, '//div[15]/div/div/div[2]/a')
    rePhone_loc = (By.XPATH, './/input[@name = "mobile"]')
    reCode_loc = (By.XPATH, '//form[@name="mixForm"]/div[2]/input')
    reGetCode_loc = (By.XPATH, '//form[@name="mixForm"]/div[2]/a')
    reNewPwd_loc = (By.XPATH, '//form[@name="mixForm"]/div[3]/input')
    reConfirmBtn_loc = (By.XPATH, '//form[@name="mixForm"]/div[6]/button[2]')
    reBackBtn_loc = (By.XPATH, '/html/body/div[15]/div/div/div[2]')
    reConfirmDialog_loc = (By.XPATH, '//div[17]/div/div/div[2]')
    reOnConfirmBtn_loc = (By.XPATH, '//div[17]/div/div/div[3]/button[2]')
    reCodeError_loc =(By.XPATH, '//form[@name="mixForm"]/div[2]/span[2]')

    # 打开登录窗口
    def open_loginWindow(self):
        print(u"打开登录窗口")
        self.driver.find_element(*LoginPage.loginBtn_loc).click()
        time.sleep(3)

    # 登录
    def login(self, username, pwd):
        print(u'输入用户名 ')
        self.driver.find_element(*LoginPage.username_loc).send_keys(username)
        time.sleep(1)
        print(u'输入密码')
        self.driver.find_element(*LoginPage.password_loc).send_keys(pwd)
        time.sleep(1)
        print(u'点击[登录]按钮')
        self.driver.find_element(*LoginPage.submitBtn_loc).click()
        time.sleep(2)

    # 切换到 忘记密码
    def click_forgotPwdBtn(self):
        print(u'点击[忘记密码]')
        self.driver.find_element(*LoginPage.forgotPwdBtn_loc).click()
        time.sleep(2)

    def resetPWD(self, rePhone, reNewPWD):
        print(u'输入手机号')
        self.driver.find_element(*LoginPage.rePhone_loc).send_keys(rePhone)
        time.sleep(2)
        print(u'输入新密码')
        self.driver.find_element(*LoginPage.reNewPwd_loc).send_keys(reNewPWD)
        time.sleep(2)
        print(u'点击[重设密码]')
        self.driver.find_element(*LoginPage.reConfirmBtn_loc).click()
        time.sleep(2)

    def resetPWD_clickCodeBtn(self):
        print(u'点击[获取验证码]')
        self.driver.find_element(*LoginPage.reGetCode_loc).click()
        time.sleep(2)

    def resetPWD_input(self, reCode):
        print(u'输入验证码')
        self.driver.find_element(*LoginPage.reCode_loc).send_keys(reCode)
        time.sleep(2)

    # 确认密码弹层
    def show_confirmDialog(self):
        print(u'弹出确认密码确认框')
        show_confirmDialog = self.driver.find_element(*LoginPage.reConfirmDialog_loc).is_displayed()
        return show_confirmDialog

    def onConfirmBtn(self):
        print(u'确认密码弹窗')
        self.driver.find_element(*LoginPage.reOnConfirmBtn_loc).click()
        time.sleep(3)

    def click_registerBtn(self):
        print(u'点击[立即注册]')

    # 断言：获取登录窗口title
    def show_loginDiaTitle(self):
        loginDialogTitle= self.driver.find_element(*LoginPage.loginDia_loc).text
        print(u'断言>>>>>>>>>当前窗口title： ' + loginDialogTitle)
        return loginDialogTitle

    # 断言：获取忘记密码窗口title
    def show_resetDiaTitle(self):
        dialogTitle = self.driver.find_element(*LoginPage.reDia_loc).is_displayed()
        return dialogTitle

    # 断言：验证码错误信息
    def show_codeError(self):
        codeError= self.driver.find_element(*LoginPage.reCodeError_loc).text
        print(u'断言>>>>>>>>>获取验证码错误提示语： ' + codeError)
        return codeError

    # 断言：弹窗消失
    # def loginWindow_closed(self):
    #     self.driver.find_element(*LoginPage.mixFrom_loc).is_displayed
    #     return True

    # 断言：登录成功
    def show_personalImgUrl(self):
        # personalImgUrl= self.driver.find_element(*LoginPage.personalImgUrl_loc).is_displayed
        personalImgUrlSrc= self.driver.find_element(*LoginPage.personalImgUrl_loc).get_attribute("src")
        print(u'断言>>>>>>>>>用户登录成功，获取头像url：' + str(personalImgUrlSrc))
        return personalImgUrlSrc

    # 断言：手机号输入框 提示信息
    def show_PhoneError(self):
       PhoneError= self.driver.find_element(*LoginPage.showPhoneError_loc).text
       print(u'断言>>>>>>>>>提示错误信息：' + PhoneError)
       return PhoneError

    # 断言：密码输入框 提示信息
    def show_PwdError(self):
       PwdError= self.driver.find_element(*LoginPage.showPwdError_loc).text
       print(u'断言>>>>>>>>>提示错误信息：' + PwdError)
       return PwdError


