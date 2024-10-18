"""
    Curves and Logs challenge
"""

ecc_a = 497
ecc_b = 1768
ecc_p = 9793    

from scalar_multiplication import ecc_scalar
from hashlib import sha1
from Crypto.Util.number import long_to_bytes

G = [1804, 5368]
Qa = [815, 3190]
nb = 1829

S = ecc_scalar(Qa, nb)
print(f"shared key : {S}")
flag = sha1(str(S[0]).encode()).hexdigest()
print(f"flag : crypto{{{flag}}}")
