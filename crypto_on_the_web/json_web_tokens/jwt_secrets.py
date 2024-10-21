"""
    JWT Secrets challenge

https://web.cryptohack.org/jwt-secrets/
"""

import jwt
import requests
base_url = "http://web.cryptohack.org/jwt-secrets"

resp = requests.get(base_url + "/create_session/" + "admin")
json_resp = resp.json()
session = json_resp["session"]

print(f"session : {session}")

key = "secret"
token = jwt.encode({'username': 'admin', 'admin': True}, key, algorithm='HS256')
print(f"new token : {token}")

decode = jwt.decode(token, key, algorithms=['HS256'])
print(f"decode : {decode}")

resp = requests.get(base_url + "/authorise/" + token + '/')
json_resp = resp.json()
if "response" in json_resp:
    output = json_resp["response"]
else:
    output = json_resp["error"]

print(f"output : {output}")