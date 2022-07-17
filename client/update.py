import requests

endpoint = 'http://localhost:8000/api/product/12/'

data = {"title":"newly"}

get_response = requests.put(endpoint, json = data)
# get_response = requests.get(endpoint)
print()
print(get_response.json())
print(get_response.status_code)