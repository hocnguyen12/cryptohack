"""
    Point Addition challenge

Algorithm for the addition of two points: P+QP+Q

(a) If P=OP=O, then P+Q=QP+Q=Q.
(b) Otherwise, if Q=OQ=O, then P+Q=PP+Q=P.
(c) Otherwise, write P=(x1,y1)P=(x1​,y1​) and Q=(x2,y2)Q=(x2​,y2​).
(d) If x1=x2x1​=x2​ and y1=−y2y1​=−y2​, then P+Q=OP+Q=O.
(e) Otherwise:
  (e1) if P≠QP=Q: λ=(y2−y1)/(x2−x1)λ=(y2​−y1​)/(x2​−x1​)
  (e2) if P=QP=Q: λ=(3x12+a)/2y1λ=(3x12​+a)/2y1​
(f) x3=λ2−x1−x2x3​=λ2−x1​−x2​
(h) y3=λ(x1−x3)−y1y3​=λ(x1​−x3​)−y1​
(i) P+Q=(x3,y3)P+Q=(x3​,y3​)
"""

from Crypto.Util.number import inverse

def ecc_add(a, b):
    # Curb Parameters
    ecc_a = 497
    ecc_b = 1768
    ecc_p = 9739

    if a == [0, 0]:
        return b
    elif b == [0, 0]:
        return a

    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    if x1 == x2 and y1 == -y2:
        return [0, 0]
    elif a != b:
        inv = inverse(x2 - x1, ecc_p)
        lbda = ((y2 - y1) * inv) % ecc_p
    else :
        inv = inverse(2 * y1, ecc_p)
        lbda = (3 * pow(x1, 2, ecc_p) + ecc_a) * inv % ecc_p

    x3 = pow(lbda, 2, ecc_p) - x1 - x2
    y3 = lbda * (x1 - x3) - y1
    return [x3 % ecc_p, y3 % ecc_p]

x = [5274, 2841]
y = [8669, 740]
print(f"x + y : {ecc_add(x, y)}")
print(f"x + x : {ecc_add(x, x)}")

p = [493, 5564]
q = [1539, 4742]
r = [4403, 5202]

s = ecc_add(ecc_add(ecc_add(p, p), q), r )
print(f"flag : crypto{{{s[0]}, {s[1]}}}")