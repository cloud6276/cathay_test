__author__ = "chavezliu"
from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome

driver = WebChrome()
driver.implicitly_wait(10)
driver.get("https://www.cathaybk.com.tw/cathaybk/")
driver.maximize_window()
time.sleep(10) #刻意延遲10秒鐘以便抓圖
driver.snapshot("cathaybk_screenshot.png")