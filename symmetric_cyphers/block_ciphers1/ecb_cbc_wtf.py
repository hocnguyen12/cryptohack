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

plaintext = ""
while True:
    iv = os.urandom(16)
    result = decrypt(ciphertext - iv.hex())
    plaintext = result["plaintext"]

    try:
        decoded_text = bytes.fromhex(plaintext).decode('utf-8')
        if "crypto" in decoded_text:
            print(decoded_text)
            break
    except(ValueError, UnicodeDecodeError):
        continue
