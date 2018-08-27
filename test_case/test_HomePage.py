'''
__data__ = 2017/8/22
__author__ = amy liu
'''

# coding = utf-8
import unittest
from congif.Mytest import Mytest
from page_obj.HomePage import HomePage
import time


class HomePageTest(Mytest):

    '''
    首页测试用例
    游客状态
    '''

    # 实例化
    homePage = HomePage()

    def test_goNavMenu(self):
        # 点击[健康管理]
        self.homePage.goPatientManage()
        self.assertTrue(self.homePage.assert_show_loginWindow(), u'登录窗口未弹出')
        self.homePage.close_loginWindow()

        # 点击[诊疗助手]
        self.homePage.goMedical()
        self.assertTrue(self.homePage.assert_show_loginWindow(), u'登录窗口未弹出')
        self.homePage.close_loginWindow()

        # 点击[一站式培训]
        self.homePage.goStudyMenu()
        self.assertIn('pica_study.html', self.homePage.get_currentUrl(), u'跳转链接错误')

        # 点击[健康漫画]
        self.homePage.goPatientEdu()
        self.assertIn('/pica_patient_edu.html', self.homePage.get_currentUrl(), u'跳转链接错误' )

        # 点击[关于云鹊医]
        self.homePage.goAboutUs()
        self.assertIn('pica_about_us.html', self.homePage.get_currentUrl(), u'跳转链接错误')

    # def test_clickCarouselImg(self):
    #     # 循环点击轮播图
    #     allcarouselImg = self.homePage.clickCarouselImg()
    #     if len(allcarouselImg )==0:
    #         print(u'未获取到轮播图')
    #     else:
    #         for carouseImg in allcarouselImg:
    #

    def test_goMainProject(self):
        # 点击进入重点项目
        self.homePage.goMainProjectLeft()
        # 切换到高血压窗口tab
        window_current = self.driver.current_window_handle
        windows = self.driver.window_handles
        for current_new in windows:
            if current_new != window_current:
                self.driver.switch_to_window(current_new)
                self.assertIn('nccd', self.homePage.get_currentUrl(), u'跳转链接错误')
        time.sleep(3)
        # 切换回到首页tab
        self.driver.switch_to_window(window_current)
        self.homePage.goMainProjectRight()
        self.assertTrue(self.homePage.assert_show_loginWindow(), u'登录窗口未弹出')







if __name__ == "__main__":
    unittest.main()







