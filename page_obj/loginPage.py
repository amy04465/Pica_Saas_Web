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
    loginButton_loc = (By.XPATH, '//*[@id="login"]/li[1]/span')
    loginDialog_loc = (By.XPATH,'//div[@ class="modal-content"]')
    loginDialogTitle_loc = (By.XPATH, '//div[@ class="modal-title"]')
    username_loc = (By.XPATH, '//form[@ name="mixForm"]/div/input[1]')
    password_loc = (By.XPATH, '//form[@ name="mixForm"]/div[3]/input[1]')
    submitButton_loc = (By.XPATH, '//form[@ name="mixForm"]/div[6]/button[1]')
    personalImgUrl_loc = (By.XPATH, '//*[@id="personalImgUrl"]')
    showPhoneError_loc = (By.XPATH, '//form[@ name="mixForm"]/div[1]/span[2]')
    showPwdError_loc = (By.XPATH, '//form[@ name="mixForm"]/div[3]/span[4]')
    # 注册
    registerButton_loc = (By.XPATH, './span/a[text() = "注册"]')
    # 忘记密码
    forgotPwdButton_loc = (By.XPATH,'./div/a[text() = "找回密码"]')

    # 打开登录窗口
    def open_loginWindow(self):
        print(u"打开登录窗口")
        self.driver.find_element(*LoginPage.loginButton_loc).click()
        time.sleep(3)

    # 登录
    def login(self, username, Password):
        print(u'输入用户名 ')
        self.driver.find_element(*LoginPage.username_loc).send_keys(username)
        time.sleep(1)
        print(u'输入密码')
        self.driver.find_element(*LoginPage.password_loc).send_keys(Password)
        time.sleep(1)
        print(u'点击[登录]按钮')
        self.driver.find_element(*LoginPage.submitButton_loc).click()
        time.sleep(2)

    # 切换到 忘记密码
    def open_forgotPwdWindow(self):
        print(u'点击[忘记密码]')
        self.driver.find_element(*LoginPage.forgotPwdButton_loc).click()
        time.sleep(3)

    def open_registerWindow(self):
        print(u'点击[立即注册]')



    # 断言：获取窗口title
    def show_loginDialogTitle(self):
        mixFromTitle= self.driver.find_element(*LoginPage.loginDialogTitle_loc).text
        print(u'断言>>>>>>>>>当前窗口title ' + mixFromTitle)
        return mixFromTitle



    # # 断言：弹窗消失
    # def loginWindow_closed(self):
    #     self.driver.find_element(*LoginPage.mixFrom_loc).is_displayed
    #     return True

    # 断言：登录成功
    def show_personalImgUrl(self):
        personalImgUrl= self.driver.find_element(*LoginPage.personalImgUrl_loc).is_displayed
        personalImgUrlSrc= self.driver.find_element(*LoginPage.personalImgUrl_loc).get_attribute("src")
        print(u'断言>>>>>>>>>用户登录成功，获取头像url：' + personalImgUrlSrc)
        return personalImgUrl

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


