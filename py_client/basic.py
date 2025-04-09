import requests

endpoint = "http://127.0.0.1:8000/products/"

response = requests.post(endpoint, params={"abc":123}, json ={"title": "Tecno", "content": "Tecno is a my Tecno", "price": 100.00})

print(response.json())
print(response.status_code)