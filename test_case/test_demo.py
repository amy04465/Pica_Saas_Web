'''
__data__ = 2017/11/24
__author__ = amy liu
'''

import time
import unittest
from selenium import webdriver

from page_obj.function import search


class KeywordsSearch(unittest.TestCase):
    def setUp(self):
        print('pass')

    def test_KeywordsSearch(self):
        search('haowan')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

