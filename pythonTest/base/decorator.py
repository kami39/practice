#-*- coding:UTF-8 -*-
'''
def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)
    return new_F

@decorator
def square_sum(a, b):
    return a**2 + b**2


@decorator
def square_diff(a, b):
    return a**2 - b**2

'''

# a new wrapper layer
def pre_str(pre=''):
    # old decorator
    def decorator(F):
        def new_F(a, b):
            print(pre + " input", a, b)
            return F(a, b)
        return new_F
    return decorator

# get square sum
@pre_str('wusz')
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@pre_str('T_T')
def square_diff(a, b):
    return a**2 - b**2


#class decoractor
def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display   = 0
            self.wrapped         = aClass(age)
        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass

@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print("My age is",self.age)



def decorator_class(classA):
    class newClass:
        def __init__(self,age):
            self.a = classA(age)
            self.num = 0
        def run(self):
            self.num+=1
            print self.num," RUN."
            self.a.run()
    return newClass
     
@decorator_class
class class_a:
    def __init__(self,age):
        self.age = age
    def run(self):
        print "age:",self.age,"run..."
 
if __name__ == "__main__":
    square_sum(1,2)
    class_a(1).run()
