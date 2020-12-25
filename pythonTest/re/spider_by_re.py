import re, requests


r = requests.get("https://www.baidu.com/")
p = re.compile(r'<img hidefocus.+?src=(.+?png).+?>')
# p = re.compile(r'<img hidefocus.+?src=\"(.+?)\".+?>')
image = p.search(r.text)
# print(image.group().split('//')[1].split()[0])
print(image.group())
print(image.group(1))


'''
s = "<img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129>"
p = re.compile(r'<img .+src=(.+png).+>')
print p.search(s).group(1)
'''