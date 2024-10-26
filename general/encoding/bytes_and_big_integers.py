"""
    Bytes and Big Integers challenge
"""

from Cryptodome.Util import number as nb

int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 
print(f"flag : {nb.long_to_bytes(int)}")
