'''
__data__ = 2017/8/22
__author__ = amy liu
'''

# coding = utf-8
# 封装部分维护在此

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from congif.Mytest import Mytest
from congif.constant import *


class BasePage(object):
    driver = Mytest.driver
    # base_url = LOGIN_URL

    # # 构造方法，用来接收selenium的driver对象
    # def __init__(self):
    #     self.driver.implicitly_wait(30)
    #     self.driver.maximize_window()
    #     self.driver.verificationErrors = []
    #     self.driver.accept_next_alert = True

    # 重写元素方法，确保元素是 可见的
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.find_element(*loc)
        except:
            print(u'%s 页面中无法找到 %s 元素' % (self, loc))

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.find_elements(*loc)
        except:
            print(u'%s 页面中无法找到 %s 元素' % (self, loc))

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)  # getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except ArithmeticError:
            print(u'%s 页面未能找到 %s 元素' % (self, loc))

    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title
