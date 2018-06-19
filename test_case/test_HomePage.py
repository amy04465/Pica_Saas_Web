'''
__data__ = 2017/8/22
__author__ = amy liu
'''

# coding = utf-8

from page_obj.HomePage import HomePage
from public.Mytest import Mytest


class HomePageTest(Mytest):
    '''
    首页测试用例
    游客状态
    '''

    # 游客状态
    # 打开首页
    def test_Open_HomePage(self):
        self.home_Page = HomePage(self.driver, self.base_url)
        self.home_Page.goHomePage()
        self.assertIn("yunqueyi.com",HomePage.get_currentUrl(self), u'url地址错误')
        # HomePage.get_currentUrl(self)
        # self.assertIn("yunqueyi.com",HomePage.currentUrl, u'url地址错误')
        # print(HomePage.currentUrl)

    def test_Open_loginWindow(self):
        # self.test_Open_HomePage()
        HomePageTest.test_Open_HomePage(self)
        # 打开登录弹窗
        # self.home_Page.open_loginWindow()
        HomePage.open_loginWindow(self)
        self.assertTrue(HomePage.assert_show_loginWindow(self), u'登录窗口未弹出')
        # self.home_Page.close_loginWindow()

    def test_goPatientManage(self):
        HomePageTest.test_Open_HomePage(self)
        # 点击[健康管理]
        # self.home_Page.goPatientManage()
        HomePage.goPatientManage(self)
        self.assertTrue(HomePage.assert_show_loginWindow(self), u'登录窗口未弹出')
        # self.home_Page.close_loginWindow()

    def test_goMedical(self):
        HomePageTest.test_Open_HomePage(self)
        # 点击[诊疗助手]
        # self.home_Page.goMedical()
        HomePage.goMedical(self)
        self.assertTrue(HomePage.assert_show_loginWindow(self), u'登录窗口未弹出')
        # self.home_Page.close_loginWindow()

    def test_goStudyMenu(self):
        HomePageTest.test_Open_HomePage(self)

        # 点击[一站式培训]
        HomePage.goStudyMenu(self)
        all_studyDropMenuOptions = HomePage.get_studyDropMenuOptions(self)
        for studyDropMenuOption in all_studyDropMenuOptions:
            if len(all_studyDropMenuOptions) == 0:
             self.assertTrue(False, msg=u'无下拉选项')
            else:
             HomePage.go_studyDropMenuOptions(self)
             print(u'循环下拉选择项：'+ studyDropMenuOption)












