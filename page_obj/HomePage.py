'''
__data__ = 2017/8/22
__author__ = amy liu
'''

#  coding = utf-8

import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from congif.base import BasePage


class HomePage(BasePage):
    # 元素维护
    PatientManage_loc = (By.LINK_TEXT, u'健康管理')
    medical_loc = (By.LINK_TEXT, u'诊疗助手')
    loginButton_loc = (By.XPATH, '//*[@id="login"]/li[1]/span')
    loginDialog_loc = (By.XPATH,'//div[@ class="modal-content"]')
    closeIcon_loc = (By.XPATH, '//*[@id = "loginClose"]')
    studyDropMenu_loc = (By.XPATH, '//div[1]/div[1]/div/div/div[2]/ul/li[2]/span')
    # 单个选项
    # studyDropMenuOptions_loc = (By.XPATH, '//div[1]/div[1]/div/div/div[2]/ul/li[2]/ul/li[3]/a')
    studyDropMenuOptions_loc = (By.XPATH, '//ul[@ id="studyDropMenu"]/li[3]/a')
    # studyDropMenuOptions_loc = (By.LINK_TEXT, u'微专业')

    # 点击[患者管理]
    def goPatientManage(self):
        print(u'点击[健康管理]')
        self.driver.find_element(*HomePage.PatientManage_loc).click()
        time.sleep(2)

    # 点击[诊疗助手]
    def goMedical(self):
        print(u'点击[诊疗助手]')
        self.driver.find_element(*HomePage.medical_loc)
        time.sleep(2)

    def goStudyMenu(self):
        print(u'点击[一站式培训]')
        # 主菜单
        studyDropMenu = self.driver.find_element(*HomePage.studyDropMenu_loc)
        ActionChains(self.driver).move_to_element(studyDropMenu).perform()
        time.sleep(4)
        self.driver.find_element(*HomePage.studyDropMenuOptions_loc).click()
        time.sleep(3)

    # def get_studyDropMenuOptions(self):
    #     studyDropMenuOptions = self.driver.find_elements(*HomePage.studyDropMenuOptions_loc)
    #     print(studyDropMenuOptions)
    #     time.sleep(2)
    #     return studyDropMenuOptions

    # def go_studyDropMenuOptions(self):
    #     # 单个选项
    #     self.driver.find_element(*HomePage.studyDropMenuOptions_loc).click()
    #     # all_studyDropMenuOptions = self.driver.find_elements(*HomePage.studyDropMenuOptions_loc).click()
    #     # print(studyDropMenuOptions.text)
    #     time.sleep(3)

    # 关闭登录弹窗
    def close_loginWindow(self):
        print(u'关闭登录窗口')
        self.driver.find_element(*HomePage.closeIcon_loc).click()
        time.sleep(2)

    # 断言
    def assert_show_loginWindow(self):
        assert_loginDialog =self.driver.find_element(*HomePage.loginDialog_loc).is_displayed
        return assert_loginDialog

    # 断言：获取当前url
    # currentUrl = ''
    def get_currentUrl(self):
        global currentUrl
        currentUrl = self.driver.current_url
        print(u'断言>>>>>>>>>当前url ' + currentUrl)
        return currentUrl









