"""
    XOR Starter challenge
"""

str = "label"
result = []

for i in range(len(str)):
    result.append(13 ^ ord(str[i]))

print(f"flag : crypto{{{''.join([chr(o) for o in result])}}}")
