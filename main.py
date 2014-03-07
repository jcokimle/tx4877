#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################################################
# Algos pour la TX + tests
# date = 06/03/14
####################################################

from random import randint
from math import log
from fractions import gcd
import unittest


# =====================================================================================
# Exponentiation rapide
# =====================================================================================

def square_pow (base,  exponent,  modulus):
    """
    Calcule base^exponent mod modulus en suivant l'algorithme d'exponentiation rapide (exponentiation by squaring)
    """    
    r = 1
    
    base = base % modulus
    while exponent > 0 :
        if (exponent % 2 ) :
            r = (r * base) % modulus
        exponent = exponent >> 1
        base = (base * base ) % modulus
    
    return r
    
    
# =====================================================================================
# Rabin Miller
# =====================================================================================

def miller_rabin( n,  k = 10):
    """
    n : nombre à tester [supposé impair et > 3]
    k : nombre d'itérations du test
    """

    s = 1
    t = (n - 1) / 2
    while t%2 == 0 :
        t /= 2
        s += 1
        
    for _ in range(k) :
        rand = randint(1,  n-1)
        y = square_pow(rand,  t,  n)
        prime = 0
        
        if (y == 1) :
            prime = 1
        
        for i in range(s):
            if (y == n - 1):
                prime = 1
                break
            else :
                y = (y * y) % n
                
        if not prime :
            return False
    
    return True
    
# =====================================================================================
#  p-1 Pollard + outils
# =====================================================================================
def primes( top ):
    """
    Retourne la liste des entiers premiers < top
    Liste codée en dur pour éviter de RabinMiller dans la majorité des cas
    """
    hard = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    if top <= 100 :
        return [x for x in hard if x < top]
    else :
        for i in range(100, top) :
            if miller_rabin(i, 30) : # miller avec une sécurité élevée : pas d'erreur probable & pas de contrainte de vitesse
                hard.append(i)
        return hard
        
        
def pm1_pollard( n ,  b, it = 10 ):
    """
    Test de factorisation
    n : nombre à factoriser
    b : seuil de friabilité
    it : nombre de tentatives
    """
    assert( b < n )
    
    while it :
        it -=1
        a = randint(1, n)
        for q in primes( b ) : 
            e = abs((log(b)) / (log(q)))
            a = square_pow(a, int(pow(q, e)), n)
        g = gcd( a-1, n )
        if 1 < g < n:
            return g
        if g == 1 :
            print('G = 1')
            continue
        if g == n:
            print('G = n')
            continue
    return 0
    
# =====================================================================================
#  Génération Nombre Premier
# =====================================================================================

def prime_gen( size ):
    """
    Génère un nombre premier de taille définie
    size : taille du nombre
    """
    # définition des limites f(size)
    bot = 10**(size-1)
    top = (10**size) - 1
    
    while True : # ajouter une limite d'essais ?
        cand = 0 
        # génération d'un nombre impair dans les limites
        while (cand % 2) == 0 :
            cand = randint(bot,  top)
        
        #test de primalité
        if miller_rabin(cand,  5):
            return cand

# =====================================================================================
# Tests unitaires
# =====================================================================================
class SquarePow_Test(unittest.TestCase):
    
    def test_RandomValue(self):
        """
        Comparaison des résultats de square_pow et la fonction pow() 
        """
        base = randint(2, 50)
        exp = randint(50, 100)
        mod = randint(10, 50)
        
        self.assertEqual(pow(base, exp, mod), square_pow(base, exp,  mod))


            

class MillerRabin_Test(unittest.TestCase):
    """
    !!! Le test de RabinMiller étant probabilistique, ces tests peuvent échouer occasionellement!!!
    """
    
    def test_PrimeCount(self):
        """
        Compte les nombres premiers sur l'intervalle [1024,2047]
        Résultat  =  137
        """
        counter = 0
        for a in range(1024, 2048):
            if miller_rabin(a) :
                counter += 1
        
        self.assertEqual(counter, 137)
        
    def test_PrimeValues(self):
        """
        Teste l'algorithme sur un ensemble de valeurs arbitraires connues comme premières
        src= http://fr.wikipedia.org/wiki/Nombre_premier
        """
        set = [13, 131071, 524287, 2147483647, 3203431780337,
                170141183460469231731687303715884105727, 
                20988936657440586486151264256610222593863921]
        for a in set :
            self.assertTrue(miller_rabin(a))
        
    def test_NotPrimeValues(self):
        """
        Teste l'algorithme sur un ensemble de valeurs arbitraires connues comme non premières
        """
        set = [4294967297, 123456789101112]
        for a in set :
            self.assertFalse(miller_rabin(a))
            
class Primes_Test(unittest.TestCase):
    def test_PrimeCount(self):
        """
        Teste le nombre de nb premiers inférieurs à 100, puis 1000
        """
        self.assertEqual(len(primes(100)),  25)
        self.assertEqual(len(primes(1000)),  168) # 0.025s à l'exécution....
        
        
# =====================================================================================
# Lancement des tests
# =====================================================================================
if __name__ == "__main__":
    unittest.main(verbosity=2)  
        
