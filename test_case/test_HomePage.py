'''
__data__ = 2017/8/22
__author__ = amy liu
'''

# coding = utf-8
from congif.Mytest import Mytest
from page_obj.HomePage import HomePage
from congif.constant import *


class HomePageTest(Mytest):

    '''
    首页测试用例
    游客状态
    '''

    # 实例化
    homePage = HomePage()

    def test_goPatientManage(self):
        # 点击[健康管理]
        self.homePage.goPatientManage()
        self.assertTrue(self.homePage.assert_show_loginWindow(), u'登录窗口未弹出')
        # self.home_Page.close_loginWindow()

    def test_goMedical(self):
        # 点击[诊疗助手]
        self.homePage.goMedical()
        self.assertTrue(self.homePage.assert_show_loginWindow(), u'登录窗口未弹出')
        # self.home_Page.close_loginWindow()

    def test_goStudyMenu(self):
        # 点击[一站式培训]
        self.homePage.goStudyMenu()
        self.assertIn('pica_study.html', self.homePage.get_currentUrl(), u'跳转链接错误')

        # 循环点击[一站式培训]下拉选择项
        # HomePage.goStudyMenu(self)
        # all_studyDropMenuOptions = HomePage.get_studyDropMenuOptions(self)
        # for studyDropMenuOption in all_studyDropMenuOptions:
        #     if len(all_studyDropMenuOptions) == 0:
        #      self.assertTrue(False, msg=u'无下拉选项')
        #     else:
        #      HomePage.go_studyDropMenuOptions(self)
        #      print(u'循环下拉选择项：'+ studyDropMenuOption.text)











