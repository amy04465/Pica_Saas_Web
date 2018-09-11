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

    # 添加已存在的患者
    def test_addPatient_existed(self):
        all_inputPhone = addPatient_PHONE
        for inputPhone in all_inputPhone:
            self.patientManagePage.addPat_btn()
            self.patientManagePage.addPat_phone(inputPhone)
            self.patientManagePage.addPat_name1()
            inputName= self.patientManagePage.get_exitedName()
            if len(inputName) != 0:
                print('-----该居民已存在-----')
                self.patientManagePage.addPat_submit()
                self.assertIn('patientInfo', self.homePage.get_currentUrl(), u'未跳转到已存在的居民详情页')
                # 返回到健康管理首页
                self.homePage.goPatientManage()

            else:
                print(u'-----该居民不存在-----')
                self.patientManagePage.addPat_name2(addPatient_NAME)
                self.patientManagePage.addPat_submit()
                self.assertTrue(self.patientManagePage.addPatSucc_dia(),u'添加居民失败')
                self.patientManagePage.close_addPatSucc_dia()

        # 断言
        # all_Patients = self.patientManagePage.get_allPatients()
        # count = 0
        # for patient in all_Patients:
        #     count= count+ patient
        #     if addPatient_NAME in all_Patients:
        #         print(u'添加成功')
        #         print(patient.text)
        #         return count

