'''
__data__ = 2017/11/24
__author__ = amy liu
'''

import time
import unittest
from selenium import webdriver


class KeywordsSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')

    def test_KeywordsSearch(self):
        self.driver.find_element_by_id('kw').send_keys(u'栗子')
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        # 断言
        self.assertIn(u'栗子', self.driver.title)
        print('---- Test Passed ----')
        print(self.driver.title + u'包含关键字[栗子]')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

