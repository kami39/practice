'''
L1 = [1,2,3]
L2 = L1
L1[0] = 10
print L2

def f(x):
    x = 100
    print x

a = 1
f(a)
print a
'''

def f(x):
    x[0] = 100
    print (x)

a = [1,2,3]
f(a)

print (a)