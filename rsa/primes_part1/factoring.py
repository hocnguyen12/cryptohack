"""
    Factoring challenge

https://factordb.com/index.php?query=510143758735509025530880200653196460532653147

details on Modern Elliptic Curve Factorization
https://programmingpraxis.com/2010/04/23/modern-elliptic-curve-factorization-part-1/
https://programmingpraxis.com/2010/04/27/modern-elliptic-curve-factorization-part-2/
"""

import primefac

N = 510143758735509025530880200653196460532653147

print("factoring...")
p = primefac.primefac(N)

print(f"flag : {p}")