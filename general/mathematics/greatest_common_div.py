"""
    Greatest Common Divisor challenge

GCD pseudo code
function gcd(a, b)
    while b ≠ 0
        t := b
        b := a mod b
        a := t
    return a
"""

def gcd(a, b):
    t = 0
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

c = 66528
d = 52920
print(gcd(8, 12))
print(f"flag : {gcd(c, d)}")