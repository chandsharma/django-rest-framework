import requests

endpoint = 'http://localhost:8000/api/product/list'

data = {"title":"create product25"}

get_response = requests.post(endpoint, json = data)
# get_response = requests.get(endpoint)
print()
print(get_response.json())
print(get_response.status_code)