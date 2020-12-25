#-*- coding: UTF-8 -*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.youdao.com")

# 获得cookie信息
cookie= driver.get_cookies()

#将获得cookie的信息打印
print cookie

driver.quit()