"""
    Modular Inverting challenge

Fermat's little theorem
a^{p - 1} = 1 mod p
a * a^{p - 2} = 1 mod p
inverse : a^{p - 2}
"""

a = 3
p = 13
d = pow(a, p - 2, p)
print(f"flag (inverse of 3 mod 13) : {d}")