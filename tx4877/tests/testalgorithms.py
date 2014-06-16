#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import gcd
from math import log
from random import randrange, randint
import unittest

from tx4877.millerrabin import MillerRabin
from tx4877.utils import square_pow, primes


class SquarePow_Test(unittest.TestCase):
    
    def test_RandomValue(self):
        """
        Comparing results between square_pow() and pow()
        """

        base = randint(2, 50)
        exp = randint(50, 100)
        mod = randint(10, 50)
        
        self.assertEqual(pow(base, exp, mod), square_pow(base, exp, mod))


            

class MillerRabin_Test(unittest.TestCase):
    """
    !!! MillerRabin is a probabilistic test which means that it can sometimes fail !!!
    """
    
    def test_PrimeCount(self):
        """
        Counts the number of primes in the interval [1024, 2047]
        The result should be 137
        """
        counter = 0
        for a in range(1024, 2048):
            mr = MillerRabin(a)
            mr.run()
            if mr.is_prime :
                counter += 1
        
        self.assertEqual(counter, 137)
        
    def test_PrimeValues(self):
        """
        Testing MR on different known prime numbers
        src= http://fr.wikipedia.org/wiki/Nombre_premier
        """
        list_primes = [13, 131071, 524287, 2147483647, 3203431780337,
                170141183460469231731687303715884105727,
                20988936657440586486151264256610222593863921]
        for a in list_primes :
            mr = MillerRabin(a)
            mr.run()
            self.assertTrue(mr.is_prime)
        
    def test_NotPrimeValues(self):
        """
        Testing MR on not prime numbers
        """
        list_not_primes = [4294967297, 123456789101112]
        for a in list_not_primes :
            mr = MillerRabin(a)
            mr.run()
            self.assertFalse(mr.is_prime)
            
class Primes_Test(unittest.TestCase):
    def test_PrimeCount(self):
        """
        Testing the number of 100- primes (25) then 1000- primes (168)
        """
        self.assertEqual(len(primes(100)), 25)
        self.assertEqual(len(primes(1000)), 168) # 0.025s à l'exécution....
        
   

if __name__ == "__main__":
    unittest.main(verbosity=2) 