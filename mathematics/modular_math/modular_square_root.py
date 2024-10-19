"""
    Modular Square Root challenge

sudo apt-get install sagemath
"""

def legendre_symbol(a, p):
    """
    Computes legendre symbol (a | p).

    (a | p) = 1 if a is a quadratic residue and a != 0 mod p
    (a | p) = -1 if a is a quadratic non-residue mod p
    (a | p) = 0 if a = 0 mod p
    """
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(n, p):
    """
    Computes modular square root of n mod p
    """
    assert legendre_symbol(n, p) == 1 # n has to be a quadratic residue

    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)

    # By factoring out powers of 2, find Q and S such that p - 1 = Q2^{S} with Q odd
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Search for a z in Z / p Z {\displaystyle \mathbb {Z} /p\mathbb {Z} } which is a quadratic non-residue 
    z = 2
    while legendre_symbol(z, p) != p - 1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)

    # If t = 0, return r = 0, If t = 1, return r = R
    while t != 0 and t != 1:
        t2i = t
        i = 0
        # Otherwise, use repeated squaring to find the least i, 0 < i < M, such that t 2 i = 1 {\displaystyle t^{2^{i}}=1}
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break

        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p

    return r


if __name__ == '__main__':
    a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768
    p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

    #import sage
    #print(sage.rings.finite_rings.integer_mod.square_root_mod_prime(a, p))

    print(f"p % 4 = {p % 4}")

    print(f"flag : {tonelli_shanks(a, p)}")