# ECB CBC WTF
from Crypto.Cipher import AES
from pwn import xor
import requests

def encrypt():
    url = "http://aes.cryptohack.org//ecbcbcwtf/encrypt_flag/"
    response = requests.get(url)
    return response.json()['ciphertext']

flag = encrypt()
f = [flag[i:i+32] for i in [0,32,64]]
print(f)
vi = f[0:(len(f)-1)]
f = f[1:]

print(vi)
print(f)
def decrypt(data):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/"
    response = requests.get(url + data + '/')
    return response.json()['plaintext']

for i in range(len(f)):
    f[i] = decrypt(f[i])

print(f)
print(vi)

for i in range(len(f)):
    f[i] = xor(bytes.fromhex(f[i]),bytes.fromhex(vi[i]))

flag = ""
print(f)
for i in f:
    flag += i.decode()

print(flag)
