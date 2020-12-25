#-*- coding: UTF-8 -*-
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time
import os

def emmail_login():
	drive = webdriver.Firefox()
	drive.get("http://mail.sina.com.cn/?from=mail")
	time.sleep(10)

	# user = drive.find_element_by_xpath("//input[@class='username']")
	user = drive.find_element_by_xpath(".//*[@id='freename']")
	# user = drive.find_element_by_class_name("username")

	time.sleep(3)
	print("1111111111111111111")
	user.clear()
	user.send_keys("wushizhang713@sina.cn")
	
	print("2222222222222222222")
	pwd = drive.find_element_by_xpath("//input[@class='password']") 
	pwd.send_keys("wushizhang713")
	pwd.send_keys(Keys.RETURN)
	time.sleep(10)


	assert u"新浪邮箱".encode('gbk') in drive.title
	print("3333333333333333333")
	logout = drive.find_element_by_xpath("//a[@_act='logout']") 
	logout.click()

	drive.close()
	drive.quit()


if __name__ == "__main__":
	emmail_login()