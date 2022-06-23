# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 11:16:11 2022

@author: User
"""
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
#print(chrome_browser)
#chrome_browser.maximize_window()
#chrome_browser.get('https://www.seleniumeasy.com/testng-tutorials')
#print('TestNG Tutorials' in chrome_browser.title)
element = chrome_browser.find_element_by_class_name('container-fluid')
print(element)