'''
__data__ = 2017/8/22
__author__ = amy liu
'''

# coding = utf-8
import unittest
from congif.Mytest import Mytest
from page_obj.HomePage import HomePage


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
        self.homePage.close_loginWindow()

    def test_goMedical(self):
        # 点击[诊疗助手]
        self.homePage.goMedical()
        self.assertTrue(self.homePage.assert_show_loginWindow(), u'登录窗口未弹出')
        self.homePage.close_loginWindow()

    def test_goStudyMenu(self):
        # 点击[一站式培训]
        self.homePage.goStudyMenu()
        self.assertIn('pica_study.html', self.homePage.get_currentUrl(), u'跳转链接错误')

    def test_goPatientEdu(self):
        # 点击[健康漫画]
        self.homePage.goPatientEdu()
        self.assertIn('/pica_patient_edu.html', self.homePage.get_currentUrl(), u'跳转链接错误' )

    def test_goAboutUs(self):
        # 点击[关于云鹊医]
        self.homePage.goAboutUs()
        self.assertIn('pica_about_us.html', self.homePage.get_currentUrl(), u'跳转链接错误')




if __name__ == "__main__":
    unittest.main()







