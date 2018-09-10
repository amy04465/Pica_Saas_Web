#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# @Time: 2018/9/3 16:25

# @FileName: test_PatManage_addPatient.py

# author: amy.liu
from congif.Mytest import Mytest
from page_obj.HomePage import HomePage
from page_obj.PatientManagePage import PatientManagePage
from page_obj.loginPage import LoginPage
from test_case.test_login import loginTest
from congif.constant import *

class PatientManagePageTest(Mytest):

    '''
    健康管理
    '''

    # 实例化
    loginTest = loginTest()
    homePage = HomePage()
    patientManagePage = PatientManagePage()

    def setUp(self):
        # 登录
        self.loginTest.test_login_success()
        # 点击【健康管理】
        self.homePage.goPatientManage()

    def test_addPatient(self):
        self.patientManagePage.addPatient()
        # 断言
        all_Patients = self.patientManagePage.get_allPatients()
        for patient in all_Patients:
            if addPatient_NAME in all_Patients:
                print(u'添加成功')

