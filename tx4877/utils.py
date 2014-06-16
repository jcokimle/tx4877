from tx4877.millerrabin import MillerRabin


_smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def primes(top):
    """
    returns the top- prime numbers
    uses and completes _smallprimes
    """
    if top <= max(_smallprimes) :
        return [x for x in _smallprimes if x < top]
    else :
        mr = MillerRabin()
        for i in range(max(_smallprimes) + 1, top):
            mr.initialize(i, 30)
            mr.run()
            if (i % 2) and mr.is_prime : 
                _smallprimes.append(i) 
        return _smallprimes
def square_pow (base, exponent, modulus):
    """
    Modular exponentiation algorithm
    Not used because pow(x, y, z) is already implemented
    """
    r = 1
    exponent = int(exponent) # fix for python3
    base = base % modulus
    while exponent > 0 :
        if (exponent % 2 ) :
            r = (r * base) % modulus
        exponent = exponent >> 1
        base = (base * base ) % modulus
    return r
