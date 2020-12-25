#coding=utf-8
import os.path
import glob

path = 'E:\WUSZ\py_prj\os\os_module.py'


print(os.path.basename(path)) #文件路径
print(os.path.dirname(path))  #文件目录

print(os.path.exists(path))    # 查询文件是否存在

print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件

#print(os.path.split(path))	# 将路径分割成文件名和目录两个部分，放在一个表中返回

print(glob.glob('E:\WUSZ\py_prj\os\*'))