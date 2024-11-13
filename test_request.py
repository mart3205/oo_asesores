import requests

url = "http://127.0.0.1:5000/ask"
data = {
    "question": "4 tiendas con menor venta neta en marzo",
    "sessionId": "defaultSession",
    "endSession": False
}

response = requests.post(url, json=data)
print(response.json())