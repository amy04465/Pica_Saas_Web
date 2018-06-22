'''
__data__ = 2017/8/22
__author__ = amy liu
'''

# coding = utf-8
# 封装部分维护在此

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import locat_config
from log.log import Logger


class BasePage(object):
    logger = Logger()

    # 构造方法，用来接收selenium的driver对象
    @classmethod
    def __init__(cls, driver):
        cls.driver = driver

    @classmethod
    def get(cls, url):
        cls.logger.loginfo(url)
        cls.driver.get(url)

    # 重写元素方法，确保元素是 可见的
    @classmethod
    def find_element(cls, page, element):
        try:
            # 加入日志
            cls.logger.loginfo(page)

            el = WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located(locat_config[page][element]))
            cls.logger.loginfo(page+ 'OK')
            return el
        except:
            print(u'%s 页面中无法找到 %s 元素' % (cls, element))

    @classmethod
    def find_elements(cls, page, element):
        try:
            # 加入日志
            cls.logger.loginfo(page)

            WebDriverWait(cls.driver, 10).until(EC.visibility_of_element_located(locat_config[page][element]))
            els = cls.driver.find_elements(*locat_config[page][element])
            return els
        except:
            print(u'%s 页面中无法找到 %s 元素' % (cls, element))

    @classmethod
    def send_keys(cls, page, element, value, clear_first=True, click_first=True):
        try:
            element = getattr(cls, '_%s' % element)  # getattr相当于实现self.loc
            if click_first:
                el = cls.find_element(page, element)
                el.click()
            if clear_first:
                el = cls.find_element(page, element)
                el.clear()
                el = cls.find_element(page, element)
                el.send_keys(value)
        except ArithmeticError:
            print(u'%s 页面未能找到 %s 元素' % (cls, element))

    # def click(self, loc):
    #     self.find_element(*loc).click()

    # click method
    @classmethod
    def click(cls, page, element):
        el = cls.find_element(page, element)
        el.click()

    #
    # def get_title(self):
    #     return self.driver.title
