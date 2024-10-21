"""
 ECB CBC WTF challenge
"""

from Crypto.Cipher import AES
import os
import requests
from pwn import xor
base_url = "http://aes.cryptohack.org/ecbcbcwtf"

#get the cipherText
resp = requests.get(base_url + "/encrypt_flag")
json_resp = resp.json()
ciphertext = json_resp["ciphertext"]
print(f"ciphertext : {ciphertext}")

def decrypt(ciphertext):
    resp = requests.get(base_url + "/decrypt/" + ciphertext + '/')
    return resp.json()["plaintext"]

#first_block = bytes.fromhex(ciphertext[:16])
print(len(ciphertext))
f = [ciphertext[i:i + 32] for i in range(len(ciphertext) // 32)]
print(f)
b1 = decrypt(f[2])
print(f"first decrypted block : {decrypt(f[2])}")

plaintext = []
plaintext.append(xor(bytes.fromhex(f[1]), bytes.fromhex(b1)))
b2 = decrypt(f[1])
plaintext.append(xor(b2, f[0]))
b3 = decrypt(f[0])
#plaintext.append(xor())

print("plaintext :", plaintext)
print(plaintext[0].hex())

flag = ""
for i in range(len(plaintext), -1):
    flag += plaintext[i].hex()

print(f"flag : {flag}")