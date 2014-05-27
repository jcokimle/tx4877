from fractions import gcd
from math import log
from random import randint

from utils import primes


class Pm1Pollard(object):

    def __init__(self, n=0, b=0, it=10):
        self.initialize(n, b, it)

    def initialize(self, n, b, it):
        self.n = n
        self.b = b
        self.it = it
        self.a = 0
        self.g = 0
        self.is_prime = False
        self.is_over = False
        if n < 2:
            self.is_over = True
        self.r, self.s = 0, self.n - 1
        while self.s % 2 == 0:
            self.r += 1
            self.s //= 2

    def run(self):
        while not self.is_over:
            self.step()

    def step(self):
        if self.it and not self.is_over:
            self.it -=1
            n = self.n
            b = self.b
            self.a = randint(1, n)
            for q in primes(b) : 
                e = abs((log(b)) / (log(q)))
                self.a = pow(self.a, int(pow(q, e)), n)
            self.g = gcd(self.a - 1, n)
            if 1 < self.g < n:
                self.is_over = True
                print('Factorisation réussie : {}'.format(self.g))
            if self.g == 1 :
                # g = 1 -> augmentation du seuil et changement de a
                b += 1
        elif not self.it and not self.is_over:
            self.is_over = True
            print("Nombre d'itération max atteint. Echec de la factorisation")

    def get_state(self):
        return "It: %d - N: %d - B: %d - A: %d - G: %d - Is Over: %d" % (self.it, self.n, self.b, self.a, self.g, self.is_over)

if __name__ == "__main__":
    pm = Pm1Pollard()
    pm.initialize(4037391011150378392273634800292119677851, 1, 100000)
    pm.run()
    print(pm.get_state())
