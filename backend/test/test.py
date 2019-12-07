import requests

data = {}
data['user_id'] = 1
rsp = requests.post('http://192.168.43.239:8080/user/get_by_id', json=data)
print(rsp.text)