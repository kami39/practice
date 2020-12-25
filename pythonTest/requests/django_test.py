#-*- coding: UTF-8 -*-

import requests
import unittest

class MyTestSuite(unittest.TestCase):
	def test(self):
		url = "http://127.0.0.1:8089/users/user_login/"
		user = {'Username':'django','Password':'djangoisgood'}
		headers = {'content-type':'text/html'}
		r = requests.get(url,headers=headers,params=user)
		print (r.status_code)


	def user_login_test(self):
		url = "http://127.0.0.1:8089/users/user_login/"
		r = requests.get(url)
		print(r.status_code)
		# print(r.cookies)
		# print(r.json)


	def post(self):
		url = "http://127.0.0.1:8089/users/user_login/"
		cookie = "csrftoken="+''.join("HVMf2vCzSshg7V3R4UfvbfntS9VgsYwK")
		headers = {'Content-Type':'text/html','Cookie':cookie}

		r = requests.post(url,headers=headers)
		print(r.status_code)
		# print(dir(r))
		

def get_image():
	ir = requests.get("https://sfault-avatar.b0.upaiyun.com/326/088/3260887228-56d3ced31fdff_big64")
	sz = open('logo.jpg','wb').write(ir.content)
	# r = requests.get("")
	# p = re.compile("")
	# image = p.findall(r.text)[0]
	# ir = requests.get(image)



def test_suite():
	suite = unittest.TestSuite()
	suite.addTest(MyTestSuite("test"))
	suite.addTest(MyTestSuite("user_login_test"))
	suite.addTest(MyTestSuite("post"))

	runner = unittest.TextTestRunner()
	runner.run(suite)

if __name__ == "__main__":
	get_image()


