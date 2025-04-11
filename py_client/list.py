import requests
from getpass import getpass
from rest_framework import status

auth_endpoint = "http://127.0.0.1:8000/products/auth/"
list_endpoint = "http://127.0.0.1:8000/products/list/"

data = {
    "username": input("Enter your username: "),
    "password": getpass("Enter your password: ")
}

auth_response = requests.post(auth_endpoint, json = data)

if auth_response.status_code == status.HTTP_200_OK:
    token = auth_response.json().get("token")
    print(token)

    headers={"Authorization": f"Bearer {token}"}

    list_response = requests.get(
        list_endpoint,
        headers = headers
    )

    if list_response.status_code == status.HTTP_200_OK:
        print("Products retrieved successfully:")
        print(list_response.json())
    else:
        print("Failed to retrieve products:", list_response.status_code, list_response.json())

# print(response.json())
# print(response.status_code)