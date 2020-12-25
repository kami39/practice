import re
 
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
 
print p.match(s).group(1).title()
print p.match(s).group(2)
print p.sub(r'\2 \1', s)