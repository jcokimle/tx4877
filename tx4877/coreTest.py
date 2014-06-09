#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange, randint
from math import log
from fractions import gcd
import unittest

#instanciation du core
from core import Core
c = Core()


class SquarePow_Test(unittest.TestCase):
    
    def test_RandomValue(self):
        """
        Comparaison des résultats de square_pow et la fonction pow() 
        """


        base = randint(2, 50)
        exp = randint(50, 100)
        mod = randint(10, 50)
        
        self.assertEqual(pow(base, exp, mod), c.square_pow(base, exp,  mod))


            

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
            if c.miller_rabin(a) :
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
            self.assertTrue(c.miller_rabin(a))
        
    def test_NotPrimeValues(self):
        """
        Teste l'algorithme sur un ensemble de valeurs arbitraires connues comme non premières
        """
        set = [4294967297, 123456789101112]
        for a in set :
            self.assertFalse(c.miller_rabin(a))
            
class Primes_Test(unittest.TestCase):
    def test_PrimeCount(self):
        """
        Teste le nombre de nb premiers inférieurs à 100, puis 1000
        """
        self.assertEqual(len(c.primes(100)),  25)
        self.assertEqual(len(c.primes(1000)),  168) # 0.025s à l'exécution....
        
   

if __name__ == "__main__":
    unittest.main(verbosity=2)  
