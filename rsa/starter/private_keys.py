"""
    Private Keys challenge
"""

p = 857504083339712752489993810777
q = 1029224947942998075080348647219 

e = 65537
totient = (p - 1) * (q - 1)

# from general/mathematics/modular_inverting.py
#d = pow(e, totient - 2, totient)
# -> does not work because totient is not a prime

# from general/mathematics/extended_gcd.py
def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        quot = old_r // r
        old_r, r = r, old_r - quot * r
        old_s, s = s, old_s - quot * s
        old_t, t = t, old_t - quot * t
    return old_t, old_s # Bezout Coefficients

d = extended_gcd(e, totient)

print(f"extended_gcd(e, totient) : {d}")
print(f"flag (private key) : {max(d)}")