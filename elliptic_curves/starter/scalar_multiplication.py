"""
    Scalar Multiplication challenge

Double and Add algorithm for the scalar multiplication

Input: P∈E(Fp)P∈E(Fp​) and an integer n>0n>0
Output: Q=[n]P∈E(Fp)Q=[n]P∈E(Fp​)

1. Set Q=PQ=P and R=OR=O.
2. Loop while n > 0.
  3. If n≡1mod  2n≡1mod2, set R=R+QR=R+Q.
  4. Set Q=[2]QQ=[2]Q and n=⌊n/2⌋n=⌊n/2⌋.
  5. If n>0n>0, continue with loop at Step 2.
6. Return the point RR, which equals [n]P[n]P.
"""

ecc_a = 497
ecc_b = 1768
ecc_p = 9739

from point_addition import ecc_add
from math import floor

def ecc_scalar(p, n):
    q = p
    r = [0, 0]
    while n > 0:
        if n % 2 == 1:
            r = ecc_add(r, q)
        q = ecc_add(q, q)
        n = floor(n / 2)
    return r

if __name__ == '__main__':
    x = [5323, 5438]
    p = [2339, 2213]

    print(ecc_scalar(x, 1337))
    s = ecc_scalar(p, 7863)
    print(f"flag : crypto{{{s[0]}, {s[1]}}}")
