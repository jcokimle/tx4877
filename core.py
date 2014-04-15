#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randrange, randint
from math import log
from fractions import gcd


class Core :
	"""
	Contient l'ensemble des fonctions de calcul du programme.
	"""

	def __init__(self, file = None ):

		# liste de petits nombres premiers, utilisée par d'autres algos
		self._smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

		# log correspond
		if file != None :
			self.logFile = file
			self._log = True
		else :
			self._log = False 


	@property
	def logFile(self):
		return self._logFile

	@logFile.setter
	def logFile(self, file):
		# TODO : ajouter contrôle du path + gérer self._log
		self._logFile = file


	def square_pow (self, base,  exponent,  modulus):
	    """
	    Calcul d'exponentiation (algo d'exponentiation rapide)
	    Non utilisé car équivalent à pow()
	    """    
	    r = 1
	    exponent = int(exponent) # fix pour python3
	    base = base % modulus
	    while exponent > 0 :
	        if (exponent % 2 ) :
	            r = (r * base) % modulus
	        exponent = exponent >> 1
	        base = (base * base ) % modulus
	    return r

	def primes( self, top ):
	    """
	    retourne la liste des nbs premiers jusqu'à top exclu.
	    utilise/complète self._smallprimes
	    """
	    
	    if top <= max(self._smallprimes) :
	        return [x for x in self._smallprimes if x < top]
	    else :
	        for i in range(max(self._smallprimes)+1, top): 
	            if (i % 2) and self.miller_rabin(i, 30) : # miller avec une sécurité élevée : pas d'erreur probable & pas de contrainte de vitesse
	                self._smallprimes.append(i) 
	        return self._smallprimes


	def miller_rabin(self, n, k=10):
	    """
	    Test de pseudo-primalité Rabin-Miller
	    k est le nombre de tentatives
	    """
	    if n < 2: return False
	    for p in self._smallprimes:
	        if n < p * p: return True
	        if n % p == 0: return False
	    r, s = 0, n - 1
	    while s % 2 == 0:
	        r += 1
	        s //= 2
	    for _ in range(k):
	        a = randrange(2, n - 1)
	        x = pow(a, s, n)
	        if x == 1 or x == n - 1:
	            continue
	        for _ in range(r - 1):
	            x = pow(x, 2, n)
	            if x == n - 1:
	                break
	        else:
	            return False
	    return True

	def pm1_pollard( self, n ,  b, it = 10 ):
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
	        for q in self.primes( b ) : 
	            e = abs((log(b)) / (log(q)))
	            a = pow(a, int(pow(q, e)), n)
	        g = gcd( a-1, n )
	        if 1 < g < n:
	            print('Factorisation réussie : {}'.format(g))
	            return g
	        if g == 1 :
	            # g = 1 -> augmentation du seuil et changement de a
	            b += 1
	            print('Echec factorisation, augmentation du seuil B ({})'.format(b))
	            continue
	        if g == n:
	            # g = n -> nouvel essai avec changement de a
	            print('Echec factorisation')
	            continue
	    
	    print("Nombre d'itération max atteint. Echec de la factorisation")
	    return 0
    

	def prime_gen( self, size ):
	    """
	    Génère un nombre premier de taille définie
	    size : taille du nombre ( size > 1 )
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
	        if self.miller_rabin(cand,  5):
	            return cand




if __name__=="__main__":
	print("Nothing to do here...")
	c = Core("trace.log")
	for i,n in enumerate(c.primes(100)) :
		print("{}\t{}".format(i,n))