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


