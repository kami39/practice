from bs4 import BeautifulSoup
import re

html_doc = """  
<html><head><title>The Dormouse's story</title></head>  
<body>  
<p class="title"><b>The Dormouse's story</b></p>  
  
<p class="story">Once upon a time there were three little sisters; and their names were  
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,  
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;  
and they lived at the bottom of a well.</p>  
  
<p class="story">...</p>  
"""  

soup = BeautifulSoup(html_doc,"html.parser")
# print(soup.prettify())
# print(soup.title)
# print(soup.p.string)
# print(soup.a['href'])
# print(soup.head.contents[0])


# print(soup.find_all(["a","b"]))
# print(soup.find_all(id="link2"))
# print(soup.find_all("p","title")[0].string)
# print(soup.find(text=re.compile("sisters")) ) 




# for string in soup.strings:
# 	print(repr(string))
	# print(string)
# print(soup.select('a[href="http://example.com/elsie"]'))

def find_tag_for_text(text,content):
	soup = BeautifulSoup(text,"html.parser")
	lists=soup.find_all('a')
	print(lists)

	for list in lists:
		if list.string == content:
			print(list)
			return (list)


print(find_tag_for_text(html_doc,"Tillie")['href'])
print(soup.find_all('a',{'id':'link3'})[0]['href'])


