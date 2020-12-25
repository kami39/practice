#coding=utf8
'''
class SampleMore(object):
    def __call__(self, a):
        return a + 5

add = SampleMore()     # A function object
print(add(2))          # Call function    
print(map(add, [2, 4, 5]))    # Pass around function object
'''
# f=open("time.py",'w')
# print(dir(f))

# a = [1, 2, 3]
# print a.__class__
# print a.__class__.__name__

print("%+10x" % 10)
print("%04d" % 5)
print("%6.3f" % 2.3)
print("i am %s. %s"  % ('aaa','sss'))
print("%(name)s,  %(age)d"% {'name':"wusz",'age':18 })