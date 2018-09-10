#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# @Time: 2018/8/31 16:11

# @FileName: PatientManagePage.py

# author: amy.liu

import time
from selenium.webdriver.common.by import By
from congif.base import BasePage
from congif.constant import *


class PatientManagePage(BasePage):
    # 元素维护
    addPatient_loc = (By.XPATH, './/button[text()="添加居民"]')
    phoneText_loc = (By.XPATH, './/form/div[1]/div[1]/input')
    nameText_loc = (By.XPATH, './/form/div[3]/div[1]/input')
    confirmAdd_loc = (By.XPATH, './/button[text()="确认添加"]')
    cancelAdd_loc = (By.XPATH, '//button[text()="取消"]')
    qrCode_loc = (By.XPATH, '//img')
    patientValues_loc = (By.XPATH, '//*div[@class="card-content"]/div[2]/dl/dt')

    def addPatient(self):
        print(u'点击[添加居民]')
        self.driver.find_element(*PatientManagePage.addPatient_loc).click()
        time.sleep(3)
        print(u'输入手机号')
        self.driver.find_element(*PatientManagePage.phoneText_loc).send_keys(addPatient_PHONE)
        time.sleep(2)
        print(u'输入姓名')
        self.driver.find_element(*PatientManagePage.nameText_loc).click()
        time.sleep(2)
        self.driver.find_element(*PatientManagePage.nameText_loc).clear()
        time.sleep(2)
        self.driver.find_element(*PatientManagePage.nameText_loc).send_keys(addPatient_NAME)
        time.sleep(2)
        print(u'点击[确认添加]')
        self.driver.find_element(*PatientManagePage.confirmAdd_loc).click()
        time.sleep(3)

    # 断言：获取所有居民列表

    def get_allPatients(self):
        allPatients = self.driver.find_elements(*PatientManagePage.patientValues_loc)
        print(u'获取居民列表：' + allPatients.text)
        return allPatients



