"""
    You either know, XOR you don't
"""
enc_flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
flag_prefix = b'crypto{'

key = bytes(a ^ b for a, b in zip(enc_flag, flag_prefix))
print(f"key : {key}")

key = b'myXORkey'

flag = []
for i in range(len(enc_flag)):
    flag.append(enc_flag[i] ^ key[i % len(key)])

print(f"flag : {bytes(flag).decode('utf-8')}")

