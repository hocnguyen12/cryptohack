"""
 Modes of Operation challenge
"""

import requests
base_url = "http://aes.cryptohack.org/block_cipher_starter"

#get the cipherText
resp = requests.get(base_url + "/encrypt_flag")
json_resp = resp.json()
cipherText = json_resp["ciphertext"]
print(f"ciphertext : {cipherText}")

#decrypt the cipher text and get the plaintext
resp = requests.get(base_url + "/decrypt/" + cipherText)
plain = resp.json()["plaintext"]

#now convert the plaintext from hex to string
key = bytes.fromhex(plain).decode("utf8")
print(key)