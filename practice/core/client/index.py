import requests

endpoint = "http://127.0.0.1:8000/api/"

data = requests.post(
    endpoint, json={"title": "hello World", "content": "I do not like you", "price": 10}
)
print(data.json())
