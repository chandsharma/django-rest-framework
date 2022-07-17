import requests

endpoint = 'http://localhost:8000/api/product/'

data = {"title":"create product21"}

get_response = requests.post(endpoint, json = data)
# get_response = requests.get(endpoint)
print()
print(get_response.json())
print(get_response.status_code)