'''
Created on '2017/1/13'
@author: 'amy liu'
'''
# coding = utf-8
from selenium import webdriver
import os


def browser(selecctBrowser):
    if selecctBrowser ==1:
        # start chrome public
        chrome_driver = os.path.abspath("D:\Program Files\Python3\chromedriver.exe")
        os.environ['webdriver.chrome.public'] = chrome_driver
        driver = webdriver.Chrome(chrome_driver)

    elif selecctBrowser==2:
        # start firefox public
        driver = webdriver.Firefox()

    return driver

if __name__ == '__main__':
    dr = browser()
