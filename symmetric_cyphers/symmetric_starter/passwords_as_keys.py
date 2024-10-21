"""
 Password as keys challenge
 FLAG : crypto{k3y5__r__n07__p455w0rdz?}
"""

from Crypto.Cipher import AES
import hashlib
import random

import requests
base_url = "http://aes.cryptohack.org/passwords_as_keys"

#get the cipherText
resp = requests.get(base_url + "/encrypt_flag")
json_resp = resp.json()
ciphertext = json_resp["ciphertext"]
print(f"ciphertext : {ciphertext}")

with open("words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

#KEY = hashlib.md5(keyword.encode()).digest()

#@chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


plaintext = ""
while True:
    keyword = random.choice(words)
    hash = hashlib.md5(keyword.encode()).digest()
    result = decrypt(ciphertext, hash.hex())
    plaintext = result["plaintext"]

    try:
        decoded_text = bytes.fromhex(plaintext).decode('utf-8')
        if "crypto" in decoded_text:
            print(f"flag : {decoded_text}")
            break
    except(ValueError, UnicodeDecodeError):
        continue
