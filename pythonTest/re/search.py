import re
'''
s="i say, hello world,!too"
p1 = re.compile(r'w.+')
p2 = re.compile(r'w.+?')
p3 = re.compile(r'\Ai.+')

print p1.search(s).group()
print p2.search(s).group()
print p3.search(s).group()
'''

s="i say, hello world,!too\nhahahhahahahahahh\n"
p4 = re.compile(r'hello(\s.+d)')
print p4.search(s).group()
print p4.search(s).group(0)
print p4.search(s).group(1)


