import requests


payload = {'email': '15700198239@163.com', 'password': '1qaz2wsx'}
r = requests.post("http://mail.163.com/", data=payload)
print r.status_code