"""
    XOR Properties challenge
"""

import sys
import codecs

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_KEY1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_KEY1_KEY3_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") 

key2 = int.from_bytes(KEY1, "big") ^ int.from_bytes(KEY2_KEY1, "big")
key3 = int.from_bytes(KEY2_KEY3, "big") ^ key2
flag = hex(int.from_bytes(FLAG_KEY1_KEY3_KEY2, "big") ^ key2 ^ key3 ^ int.from_bytes(KEY1, "big"))

print(f"flag : {codecs.decode(flag[2:], 'hex').decode('ASCII')}")
