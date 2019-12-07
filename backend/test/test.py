import requests

#data = {}
#data['user_id'] = 1
#rsp = requests.post('http://192.168.43.239:8080/user/get_by_id', json=data)
#print(rsp.text)

data = {}
data['x'] = 7
rsp = requests.post('http://192.168.43.239:8080/test_send_receive', json=data)
print(rsp.text)