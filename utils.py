from millerrabin import MillerRabin


_smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

def primes(top):
    """
    retourne la liste des nbs premiers jusqu'à top exclu.
    utilise/complète self._smallprimes
    """
    if top <= max(_smallprimes) :
        return [x for x in _smallprimes if x < top]
    else :
        mr = MillerRabin()
        for i in range(max(_smallprimes) + 1, top):
            mr.initialize(i, 30)
            mr.run()
            if (i % 2) and mr.is_prime : # miller avec une sécurité élevée : pas d'erreur probable & pas de contrainte de vitesse
                _smallprimes.append(i) 
        return _smallprimes
