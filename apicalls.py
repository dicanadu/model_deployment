import requests
import json

url = 'http://127.0.0.1:8000/items/'
url_2 = 'http://127.0.0.1:8000/excercise/'

params = {
    'name': 'oli',
    'tags': 'first',
    'item_id': 2
}
params_exc = {
    'path': 'oli',
    'query': 'first',
    'body': 'arms'
}

print(json.dumps(params))
response = requests.post(url, data=json.dumps(params))
print(response.status_code, response.content)

response = requests.post(url_2, data=json.dumps(params_exc))
print(response.status_code, response.json()["path"])

response = requests.post("http://127.0.0.1:8000/2?query=5",
                         data=json.dumps({'value': 10,
                                          'msg': 'call me baby'}))
print(response.status_code, response.content)
#print(response.content[""])
