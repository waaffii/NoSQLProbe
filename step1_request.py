import requests
url = "http://127.0.0.1:5050/vuln-login"
payload = {"username": "alice", "password": "wrong"}

response = requests.post(url, json=payload, timeout=10)
print("Status Code:", response.status_code)
print("Response Body:", response.text)