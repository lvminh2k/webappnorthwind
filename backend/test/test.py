import requests

data = {}
data['user_id'] = 1
rsp = requests.post('http://172.16.0.198:8080/user/get_by_id', json=data)
print(rsp.text)