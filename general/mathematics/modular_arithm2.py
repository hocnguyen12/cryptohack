'''
    Modular Arithmetic challenge

In number theory, Fermat's little theorem states that if p is a prime number, 
then for any integer a, the number ap − a is an integer multiple of p. In the notation of modular arithmetic, 
this is expressed as a p ≡ a ( mod p ) . 

{\displaystyle a^{p}\equiv a{\pmod {p}}.}


If a is not divisible by p, that is, if a is coprime to p, then Fermat's little theorem is equivalent to the statement 
that ap − 1 − 1 is an integer multiple of p, or in symbols:[1][2] a p − 1 ≡ 1 ( mod p ) . 

{\displaystyle a^{p-1}\equiv 1{\pmod {p}}.}

'''

p = 17
print(pow(3, 17, p))
print(pow(5, 17, p))
print(pow(7, 16, p))

p = 65537
print(f"flag : {pow(273246787654, 65536, p)}")

