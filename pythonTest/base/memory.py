# a = 1

# print(id(a))
# print(hex(id(a)))

# from sys import getrefcount

# a = [1, 2, 3]
# print(getrefcount(a))

# b = a
# print(getrefcount(b))


# #  True
# a = 1
# b = 1
# print(a is b)

# # True
# a = "good"
# b = "good"
# print(a is b)

# # False
a = "very good morning aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
b = "very good morning aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(a is b)

# # False
# a = []
# b = []
# print(a is b)
# 
# 
# class from_obj(object):
#     def __init__(self, to_obj):
#         self.to_obj = to_obj

# b = [1,2,3]
# a = from_obj(b)
# print(id(a.to_obj))
# print(id(b))

# from sys import getrefcount

# from sys import getrefcount

# a = [1, 2, 3]
# print(getrefcount(a))

# b = [a, a]
# print(getrefcount(a))

# from sys import getrefcount

# a = [1, 2, 3]
# b = a
# print(getrefcount(b))

# del a
# print(getrefcount(b))

# a = [1,2,3]
# del a[0]
# print(a)

# from sys import getrefcount

# a = [1, 2, 3]
# b = a
# print(getrefcount(b))

# a = 1
# print(getrefcount(b))
# 
import gc
print(gc.get_threshold())
