#-*- coding:UTF-8 -*-
import re
'''
inputstr="i say, hello world,!too sashkadda select * from tables where name=:vname and id=:vid\n dkandakdakda name=Diablo\ndadkjadd id=1 \n"

p1 = re.compile(r'=(:\w+)')
p2 = re.compile(r'=(\w+)')

str1=inputstr.split('\n',1)[0]
str2=inputstr.split('\n',1)[1]
str3=str1

print(str1)
print(str2)

print p1.findall(str1)[0]
print p2.findall(str2)[0]
print"-------------"

# str3=re.subn(p1.findall(str1)[1],p2.findall(str2)[1],str3)
# # str3=re.subn(p1.findall(str1)[i],p2.findall(str2)[i],str1)
# print(str3)

for i in range(2):
	print i
	str4=re.sub(p1.findall(str1)[i],p2.findall(str2)[i],str3)
	str3=str4
	print(str4)

p3=re.compile(r'select .+')
print p3.search(str4).group()
'''



inputstr="i say, hello world,!too sashkadda select * from tables where name=:vname and id=:vid\n dkandakdakda name=Diablo\ndadkjadd id=1 \n"
p=re.compile(r'(?P<sign>\w+)=:(?P<value>\w+)(.+)(?P=sign)=(?P<value2>\w+).+',re.S)
print(p.search(inputstr).group("value"))
print re.sub(":"+p.search(inputstr).group("value"),p.search(inputstr).group("value2"),inputstr)






