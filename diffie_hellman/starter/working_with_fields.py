"""
    Working with Fields challenge

This comes from Fermat's little theorem
see general/mathematics/modular_inverting
"""

p = 991
g = 209
print(f"flag : {pow(g, p - 2, p)}")