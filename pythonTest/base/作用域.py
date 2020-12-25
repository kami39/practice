#out of the scope , invaild
# def line_conf():
#     def line(x):
#         return 2*x+1
#     print(line(5))   # within the scope


# line_conf()
# print(line(5))       # out of the scope


# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object

# b = 5
# my_line = line_conf()
# print(my_line(5)) 

#__closure__
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return line       # return a function object

# b = 5
# my_line = line_conf()
# print(my_line.__closure__)
# print(my_line.__closure__[0].cell_contents)
 
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))
