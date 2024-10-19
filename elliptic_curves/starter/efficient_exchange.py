"""
    Efficient Exchange challenge

{'iv': 'cd9da9f1c60925922377ea952afc212c', 
 'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'
} 

COMPUTE y :

Euler's criterion a^(p − 1) / 2 ≡ (a / p) ≡ 1 (mod p)
    a^(p−1)/2≡1(mod p)  (1)
Multiplying by a we get :
    a^(p+1)/2≡a(modp)   (2)
If p is of the form 4k+3, then p+14 is an integer, and from (2) we obtain
(a^(p+1)/4)^2≡a(modp).

-> if p = 3 mod 4 to get the square root of y_squared we need to compute :
    y_squared^((p + 1) / 4) mod p
"""

ecc_a = 497
ecc_b = 1768
ecc_p = 9739

xQa = 4726
nb = 6534

from scalar_multiplication import ecc_scalar

y_squared = (pow(xQa, 3) + ecc_a * xQa + ecc_b) % ecc_p
y = pow(y_squared, (ecc_p + 1) // 4, ecc_p) # because p = 3 mod 4

# Try with negative y :
#y = (- y) % ecc_p

p = [xQa, y]
S = ecc_scalar(p, nb)
print(f"y_squared : {y_squared}")
print(f"y : {y}")

print(f"y * y mod p : {(y * y) % ecc_p}")
print(f"shared secret S : {S}")

from decrypt_08c0fede9185868aba4a6ae21aca0148 import decrypt_flag

shared_secret = S[0]
iv = "cd9da9f1c60925922377ea952afc212c"
encrypted_flag = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"
print(decrypt_flag(shared_secret, iv, encrypted_flag))
