'''class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age

summer = chicken(2)

#print(bird.__dict__)
#print(chicken.__dict__)
#print(summer.__dict__)
print(summer.__class__)
print(summer.__base__)'''

#the function property()
# class bird(object):
#     feather = True

# class chicken(bird):
#     fly = False
#     def __init__(self, age):
#         self.age = age
#     def getAdult(self):
#         if self.age > 1.0: return True
#         else: return False
#     adult = property(getAdult)   # property is built-in

#the function property() v2
# summer = chicken(2)

# print(summer.adult)
# summer.age = 0.5
# print(summer.adult)

# class num(object):
#     def __init__(self, value):
#         self.value = value
#     def getNeg(self):
#         return -self.value
#     def setNeg(self, value):
#         self.value = -value
#     def delNeg(self):
#         print("value also deleted")
#         del self.value
#     neg = property(getNeg, setNeg, delNeg, "I'm negative")

# x = num(1.1)
# print(x.neg)
# x.neg = -22
# print(x.value)
# print(num.neg.__doc__)
# del x.neg


class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0: return True
            else: return False
        else: raise AttributeError(name)

summer = chicken(2)

# print(summer.adult)
summer.age = 0.5
print(summer.adult)

print(summer.male)