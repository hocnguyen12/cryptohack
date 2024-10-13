from pwn import * # pip install pwntools
import json
import codecs
import base64
from Cryptodome.Util.number import *

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode(type, encoded):
    if type == "base64":
        decoded = base64.b64decode(encoded).decode("utf-8")
    elif type == "hex":
        decoded = bytes.fromhex(encoded).decode("utf-8")
    elif type == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif type == "bigint":
        #encoded = hex(bytes_to_long(self.challenge_words.encode()))
        decoded = long_to_bytes(int(encoded, 16)).decode("utf-8")
    elif type == "utf-8":
        #encoded = [ord(b) for b in self.challenge_words]
        decoded = "".join([chr(o) for o in encoded])
    return decoded

def solve():
    level = 0
    while True:
        level += 1
        print("Level ", level)

        if level > 100:
            received = json_recv()
            return None

        received = json_recv()
        #print("Received type: ")
        #print(received["type"])
        #print("Received encoded value: ")
        #print(received["encoded"])
        
        decoded = decode(received["type"], received["encoded"])
        json_send({"decoded": decoded})

solve()
