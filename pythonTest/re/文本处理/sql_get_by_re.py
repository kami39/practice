#-*- coding:UTF-8 -*-
import re

s="haksanndandljailkenfake select * tables where name=:name and id=:id\nddnadalndsakada name='Diablo'\n djadadakdas id=1\n"
p = re.compile(r'(?P<sign>\w+)=:(?P<value1>\w+).+?(?P=sign)=(?P<value2>)',re.S)
#下标引用
# print(p.subn(r'\2 \1',s))
# print(p.subn(r'\g<2> \1',s))
# 
a=p.search(s)
print(a.group())