"""
    Montgomery's Ladder challenge

Montgomery’s binary algorithm in the group E(Fp)E(Fp​)

Input: P∈E(Fp)P∈E(Fp​) and an n-bit integer k=∑2ikik=∑2iki​ where kn−1=1kn−1​=1
Output: [k]P∈E(Fp)[k]P∈E(Fp​)

1. Set (R0,R1)(R0​,R1​) to (P,[2]P)(P,[2]P)
2. for i = n - 2 down to 0 do
3.   If ki=0ki​=0 then
4.      Set (R0,R1)(R0​,R1​) to ([2]R0,R0+R1)([2]R0​,R0​+R1​)
5.   Else:
6.      Set (R0,R1)(R0​,R1​) to (R0+R1,[2]R1)(R0​+R1​,[2]R1​)
7. Return R0R0​
"""

ecc_a = 486662
ecc_b = 1
ecc_p = pow(2, 255) - 19

from math import floor, log2
from Crypto.Util.number import inverse

def montgomery_add(P, Q):
    x1, y1 = P[0], P[1]
    x2, y2 = Q[0], Q[1]

    alpha = (y2 - y1) * inverse(x2 - x1, ecc_p)
    x3 = ecc_b * alpha - ecc_a - x1 - x2
    y3 = alpha * (x1 - x3) - y1
    return [x3 % ecc_p, y3 % ecc_p]

def montgomery_double(P):
    x1, y1 = P[0], P[1]

    alpha = (3 * pow(x1, 2, ecc_p) + 2 * ecc_a * x1 + 1) * inverse(2 * ecc_b * y1, ecc_p)
    x3 = ecc_b * alpha - ecc_a - 2 * x1
    y3 = alpha * (x1 - x3) - y1
    return [x3 % ecc_p, y3 % ecc_p]

def montgomery_ladder(P, k):
    R0, R1 = P, montgomery_double(P)

    n = floor(log2(k))
    for i in range(n - 2, -1, -1):
        if ((k >> i) & 1) == 0: # if ki = 0
            R0, R1 = montgomery_double(R0), montgomery_add(R0, R1)
        else:
            R0, R1 = montgomery_add(R0, R1), montgomery_double(R1)

    return R0

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../mathematics/modular_math'))
from modular_square_root import tonelli_shanks

if __name__ == '__main__':
    Gx = 9
    y_squared = (pow(Gx, 3, ecc_p) + ecc_a * pow(Gx, 2, ecc_p) + Gx) % ecc_p
    Gy = tonelli_shanks(y_squared, ecc_p)

    print(f"ecc_p : {ecc_p}")
    print(f"y_squared : {y_squared}")
    print(f" y (Gy) : {Gy}")
    print(f"check y*y == y_squared : {Gy * Gy}")

    Q = montgomery_ladder([Gx, Gy], 0x1337c0decafe)
    print(f"flag : crypto{{{Q[0]}}}")

