"""
    Quadratic Residues challenge

-> Square Root Modulo

What we are seeing, is that for the elements of Fp∗​, not every element has a square root. In fact, what we find is that for roughly one half of the elements of Fp∗​, there is no square root.

We say that an integer x is a Quadratic Residue if there exists an aa such that a2≡xmodp. If there is no such solution, then the integer is a Quadratic Non-Residue.
"""

ints = [14, 6, 11]
for j in range(3):
    for i in range(29):
        if pow(i, 2, 29) == ints[j]:
            print(f"flag : {min(i, (- i) % 29)}")

