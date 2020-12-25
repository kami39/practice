#-*- coding:UTF-8 -*-
import re

s="i say, hello world,!too"
p = re.compile(r'(\w+) (\w+)')
#下标引用
# print(p.subn(r'\2 \1',s))
print(p.subn(r'\g<2> \1',s))

'''
#别名引用
p = re.compile(r'(\w+) (?P<id1>\w+)')
print(p.subn(r'\g<id1> \1',s))
'''