import requests

headers = {'content-type':'application/json'}
r = requests.get("https://movie.douban.com/",headers = headers)
print(r.status_code)
