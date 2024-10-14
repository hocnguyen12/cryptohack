"""
 ECB CBC WTF challenge
"""

from Crypto.Cipher import AES
import os
import requests
base_url = "http://aes.cryptohack.org/ecbcbcwtf"

#get the cipherText
resp = requests.get(base_url + "/encrypt_flag")
json_resp = resp.json()
ciphertext = json_resp["ciphertext"]
print(f"ciphertext : {ciphertext}")

def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}

#first_block = bytes.fromhex(ciphertext[:16])
resp = requests.get(base_url + "/decrypt/" + ciphertext[:16])
first_block_dec = resp.json()["error"]
print(f"first block deciphered using ECB : {first_block_dec}")

prefix = ""
while True:
    iv = os.urandom(16)

