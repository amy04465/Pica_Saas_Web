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

    def test_Open_loginWindow(self):
        HomePageTest.test_Open_HomePage(self)
        # 打开登录弹窗
        #self.home_Page.open_loginWindow()
        HomePage.open_loginWindow(self)
        self.assertTrue(HomePage.assert_show_loginWindow(self), u'登录窗口未弹出')
        # self.home_Page.close_loginWindow()

    def test_goPatientManage(self):
        HomePageTest.test_Open_HomePage(self)
        # 点击[健康管理]
        # self.home_Page.goPatientManage()
        HomePage.goPatientManage(self)
        self.assertTrue(HomePage.assert_show_loginWindow(self), u'登录窗口未弹出')
        #self.home_Page.close_loginWindow()

    def test_goMedical(self):
        HomePageTest.test_Open_HomePage(self)
        # 点击[诊疗助手]
        #self.home_Page.goMedical()
        HomePage.goMedical(self)
        self.assertTrue(HomePage.assert_show_loginWindow(self), u'登录窗口未弹出')
        #self.home_Page.close_loginWindow()




