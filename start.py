import requests

url = 'http://127.0.0.1:5000/register'
myobj = {'datatype': 'registerRequest', 'id': 'N1701D', 'name': "Enterprise", "type": 'dreadnought'}

x = requests.post(url, data = myobj)

print(x.text)