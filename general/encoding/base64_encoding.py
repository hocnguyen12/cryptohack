"""
    Base64 challenge
"""

import base64

hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

flag = base64.b64encode(bytes.fromhex(hex))

print(f"b64 encoded : {flag}")

# replace + with _
# replace first / with {
# replace second / with }
print(f"flag : {str(flag).replace('/', '{', 1).replace('/', '}', 1).replace('+', '_')}")
