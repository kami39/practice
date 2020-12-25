'''

#range()
S = 'abcdefghijk'
for i in range(0,len(S),2):
    print S[i]
#enumrate()
S = 'abcdefghijk'
for (index,char) in enumerate(S):
    print(index,char) 

#zip()
ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c)
'''

'''
L = []
for x in range(10):
    L.append(x**2)
print(L)
'''

G = (x for x in range(4))
for i in G:
    print (i)
    