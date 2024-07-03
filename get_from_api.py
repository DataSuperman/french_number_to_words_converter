import requests

url = "http://127.0.0.1:8000/convert"
data = {"numbers": [17, 21, 100, 2000, 999999]}
response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")