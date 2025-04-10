import requests

endpoint = "http://127.0.0.1:8000/products/list/"

data = {
    "title": "Infinix 1", 
    # "content": "This is my infinix", 
    # "price": 100.00
    }

response = requests.get(endpoint, params={"abc":123}, json = data)

print(response.json())
print(response.status_code)