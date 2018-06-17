'''
__data__ = 2017/8/22
__author__ = amy liu
'''

#  coding = utf-8

import time
from selenium.webdriver.common.by import By
from page_obj.base import BasePage


class HomePage(BasePage):
    # 元素维护
    PatientManage_loc = (By.LINK_TEXT, u'健康管理')
    medical_loc = (By.LINK_TEXT, u'诊疗助手')
    loginButton_loc = (By.XPATH, '//*[@id="login"]/li[1]/span')
    loginDialog_loc = (By.XPATH,'//div[@ class="modal-content"]')
    closeIcon_loc = (By.XPATH, '//*[@id = "loginClose"]')

    # 初始化
    def __int__(self, driver, base_url):
        BasePage.__init__(self, driver, base_url)

    # 打开首页
    def goHomePage(self):
        print(u'打开首页url: ', self.base_url)
        self.driver.get(self.base_url)
        time.sleep(2)

    # 点击[患者管理]
    def goPatientManage(self):
        print(u'点击[健康管理]')
        self.driver.find_element(*HomePage.PatientManage_loc).click()
        time.sleep(2)

    # 点击[诊疗助手]
    def goMedical(self):
        print(u'点击[诊疗助手]')
        self.driver.find_element(*HomePage.medical_loc).click()
        time.sleep(2)

    # 打开登录窗口
    def open_loginWindow(self):
        print(u'打开登录窗口')
        self.driver.find_element(*HomePage.loginButton_loc).click()
        time.sleep(2)

    # 关闭登录弹窗
    def close_loginWindow(self):
        print(u'关闭登录窗口')
        self.driver.find_element(*HomePage.closeIcon_loc).click()
        time.sleep(2)

    # 断言
    def assert_show_loginWindow(self):
        self.driver.find_element(*HomePage.loginDialog_loc).is_displayed
        return True









