#-*- coding: UTF-8 -*-

import urllib
import requests
from bs4 import BeautifulSoup

def pic_get():
	r = requests.get("https://movie.douban.com/")
	bs = BeautifulSoup(r,"html.parser")
	# bs = BeautifulSoup(r.text,"html.parser")

	image = bs.find("img",alt="一条狗的使命")['src']
	print(image)
	urllib.urlretrieve(image,"./dog.jpg")

if __name__ == "__main__":
	pic_get()
