
from random import randint

from millerrabin import MillerRabin


class PrimeGen(object):

    def __init__(self, size=1):
        self.mr = MillerRabin()

    def initialize(self, size):
        self.size = size
        self.bot = 10 ** (size - 1)
        self.top = (10 ** size) - 1
        self.cand = 0
        self.is_prime = False
        self.step_by_step = False
        self.not_prime = []

    def run(self):
        while not self.is_prime:
            self.step()

    def step(self):
        self.step_by_step = True
        bot = self.bot
        top = self.top

        self.cand = randint(bot,  top)
        # génération d'un nombre impair dans les limites
        while ((self.cand % 2) == 0 or self.cand in self.not_prime):
            self.cand = randint(bot,  top)
        
        #test de primalité
        self.mr.initialize(self.cand,3)
        self.mr.run()
        self.is_prime = self.mr.is_prime
        if not self.is_prime:
            self.not_prime.append(self.cand)

    def get_prime(self):
        return self.cand

    def get_state(self):
        return "Size: %d - Number: %d - Prime: %d" % (self.size, self.cand, self.is_prime)

if __name__ == "__main__":
    pm = PrimeGen()
    pm.initialize(1)
    pm.run()
    while pm.cand != 126739:
        pm.initialize(1)
        pm.run()
    print(pm.get_state())
