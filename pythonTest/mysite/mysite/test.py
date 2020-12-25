import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print (BASE_DIR)

print('--------------------------------')
a={'DIRS': [os.path.join(BASE_DIR, 'templates/west'),os.path.join(BASE_DIR, 'templates/users'),],}
b={'DIRS': (os.path.join(BASE_DIR, 'templates/west'),os.path.join(BASE_DIR, 'templates/users'),),}
print(a['DIRS'])
print(b['DIRS'])