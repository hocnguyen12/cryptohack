str = "label"
result = []

for i in range(len(str)):
    result.append(13 ^ ord(str[i]))

print("".join([chr(o) for o in result]))
