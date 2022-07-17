import requests

endpoint = 'http://localhost:8000/api/product/1/'

# get_response = requests.post(endpoint, json = {"title":None}, params={"user":'admin','pass':88888888})
get_response = requests.get(endpoint)
print()
print(get_response.json())
print(get_response.status_code)