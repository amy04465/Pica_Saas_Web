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
    # 添加居民弹层
    addPat_loc = (By.XPATH, './/button[text()="添加居民"]')
    phoneText_loc = (By.XPATH, './/form/div[1]/div[1]/input')
    nameText_loc = (By.XPATH, './/form/div[3]/div[1]/input')
    confirmAdd_loc = (By.XPATH, './/button[text()="确认添加"]')
    cancelAdd_loc = (By.XPATH, '//button[text()="取消"]')
    qrCode_loc = (By.XPATH, '//img')
    patValues_loc = (By.XPATH, '//*div[@class="card-content"]/div[2]/dl/dt')
    # 添加居民成功- 提示信息框
    addSuccDia_loc = (By.XPATH, '//*[@id="model-modify"]/div/div')
    addSuccDiaX_loc = (By.XPATH, '//*[@id="model-modify"]/div/div/div[1]/button')

    # 点击【添加居民】按钮
    def addPat_btn(self):
        print(u'点击[添加居民]')
        self.driver.find_element(*PatientManagePage.addPat_loc).click()
        time.sleep(3)

    def addPat_phone(self, addPatientPhone):
        print(u'输入手机号:' + addPatientPhone)
        self.driver.find_element(*PatientManagePage.phoneText_loc).send_keys(addPatientPhone)
        time.sleep(2)

    # 点击输入框
    def addPat_name1(self):
        self.driver.find_element(*PatientManagePage.nameText_loc).click()

    # 输入姓名
    def addPat_name2(self, addPatientName):
        print(u'输入姓名:' + addPatientName)
        self.driver.find_element(*PatientManagePage.nameText_loc).send_keys(addPatientName)
        time.sleep(3)

    # 获取姓名
    def get_exitedName(self):
        inputNameValue = self.driver.find_element(*PatientManagePage.nameText_loc).get_attribute("value")
        print(u'获取已存在的用户名：' + inputNameValue)
        return inputNameValue

    def addPat_submit(self):
        print(u'点击[确认添加]')
        self.driver.find_element(*PatientManagePage.confirmAdd_loc).click()
        time.sleep(3)

    # 添加居民成功- 提示框
    def addPatSucc_dia(self):
        print(u'弹出[添加成功]提示框')
        addSuccessDia = self.driver.find_element(*PatientManagePage.addSuccDia_loc).is_displayed()
        return addSuccessDia

    # 关闭【添加居民成功- 提示框】
    def close_addPatSucc_dia(self):
        print(u'关闭弹窗')
        self.driver.find_element(*PatientManagePage.addSuccDiaX_loc).click()
        time.sleep(2)


    # 断言：获取所有居民列表
    def get_allPats(self):
        allPatients = self.driver.find_elements(*PatientManagePage.patValues_loc)
        print(u'获取居民列表：' + allPatients.text)
        return allPatients



