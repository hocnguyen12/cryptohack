"""
    Public Keys challenge
"""

e = 65537
p = 17
q = 23
print(f"flag : {pow(12, e, p * q)}")