#-*- coding: UTF-8 -*-
from selenium import webdriver
import time

drive = webdriver.Firefox()
drive.get("http://mail.163.com/")
time.sleep(10)

#切换iframe
# drive.switch_to_frame("x-URS-iframe")
drive.switch_to.frame("x-URS-iframe")

# iframe = drive.find_element_by_xpath("//div[@id='loginDiv']/iframe")
# print (iframe.get_attribute('id'))
# drive.switch_to_frame(iframe)
print("1111111111111111111111111")

drive.find_element_by_xpath("//input[@name='email']").send_keys('123')
drive.find_element_by_xpath("//input[@name='password']").send_keys('456')

drive.switch_to_default_content()
print("2222222222222222222222222")