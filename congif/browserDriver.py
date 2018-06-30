'''
Created on '2017/1/13'
@author: 'amy liu'
'''
# coding = utf-8
from selenium import webdriver
import os


def browser(select_Browser):
    if select_Browser ==1:
        # start chrome constant
        # 引入 chromedriver
        chrome_driver = os.path.abspath("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        os.environ['webdriver.chrome.constant'] = chrome_driver
        select_Browser = webdriver.Chrome(chrome_driver)

    elif select_Browser==2:
        # start firefox constant
        select_Browser = webdriver.Firefox()

    return select_Browser

if __name__ == '__main__':
    dr = browser(1)
