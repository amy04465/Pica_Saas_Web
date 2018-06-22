# Created by AmyLiu on 18/6/22
from constant.basecopy import BasePage
from constant.browserDriver import browser
from constant.constant import LOGIN_URL


def search(msg):
    driver = browser(2)
    uihandle = BasePage(driver)
    uihandle.get(LOGIN_URL)
    uihandle.send_keys('百度首页', '搜索输入框', msg)
    uihandle.click('百度首页', '确认按钮')
