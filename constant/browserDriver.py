'''
Created on '2017/1/13'
@author: 'amy liu'
'''
# coding = utf-8
from selenium import webdriver
import os


def browser(selecct_Browser):
    if selecct_Browser ==1:
        # start chrome constant
        # 引入 chromedriver
        chrome_driver = os.path.abspath("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        os.environ['webdriver.chrome.constant'] = chrome_driver
        selecct_Browser = webdriver.Chrome(chrome_driver)

    elif selecct_Browser==2:
        # start firefox constant
        selecct_Browser = webdriver.Firefox()

    return selecct_Browser

if __name__ == '__main__':
    dr = browser(1)
