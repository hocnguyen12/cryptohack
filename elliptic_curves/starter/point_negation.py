"""
    Point Negation challenge
"""

p = 9739

xp = 8045
yp = 6936

# Q = - P

xq = xp 
yq = - yp % p

print(f"equation right side : {(pow(xq, 3) + 497 * xq + 1768) % p}")
print(f"equation left side : {pow(yq, 2) % p}")

print(f"flag : crypto{{{xq}, {yq}}}")