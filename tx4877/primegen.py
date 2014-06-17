
from random import randint
import time

from tx4877.millerrabin import MillerRabin


class PrimeGen(object):

    def __init__(self, size=1):
        self.mr = MillerRabin()
        self.initialize(size)

    def initialize(self, size):
        '''
        Initializes the variables
        '''
        self.log_msg = ""
        self.size = size
        self.bot = 10 ** (size - 1)
        self.top = (10 ** size) - 1
        self.cand = 0
        self.cpt = 1
        self.nb_mr_tests = 5
        self.is_prime = False
        self.is_over = False
        self.step_by_step = False
        self.not_primes = []
        self.log("Running Prime Gen: Size = %d" % (self.size))

    def run(self):
        '''
        Iterates until the end of the algorithm
        '''
        while not self.is_prime:
            self.step()

    def step(self):
        '''
        Computes only 1 iteration
        Adds logs at each step
        '''
        if not self.step_by_step and not self.is_over:
            self.step_by_step = True
            self.start_time = time.time()
        if not self.is_over:
            bot = self.bot
            top = self.top
            
            offset = 10
            self.log("Iteration %d" % (self.cpt), offset)
            self.cpt += 1
    
            self.cand = randint(bot,  top)
            self.log("Generating random integer of size %d: R = %d" % (self.size, self.cand), offset * 2)
            # génération d'un nombre impair dans les limites
            while ((self.cand % 2) == 0 or self.cand in self.not_primes):
                self.log("R is even or composite, try an other one", offset * 2)
                self.cand = randint(bot,  top)
                self.log("Generating random integer of size %d: R = %d" % (self.size, self.cand), offset * 2)
            
            #test de primalité
            self.log("Running Miller Rabin: N = %d, K = %d" % (self.cand, self.nb_mr_tests), offset * 2)
            self.mr.initialize(self.cand, self.nb_mr_tests)
            self.mr.run()
            self.is_prime = self.mr.is_prime
            if self.is_prime:
                self.step_by_step = False
                self.is_over = True
                self.log("%d is Prime => End" % (self.cand))
                self.log("Duration: %fs" % (time.time() - self.start_time))
            elif not self.is_prime:
                self.log("%d is Composite => Continue" % (self.cand), offset * 2)
                self.not_primes.append(self.cand)

    def log(self, msg, offset=0):
        '''
        Logs a message
        '''
        for _ in range(offset):
            self.log_msg = self.log_msg + " "
        self.log_msg = self.log_msg + msg + "\n"

    def get_state(self):
        '''
        Retuns the current state with all the variables
        '''
        return "Size: %d - Number: %d - Prime: %d" % (self.size, self.cand, self.is_prime)

''' Testing the algorithm '''
if __name__ == "__main__":
    pm = PrimeGen()
    pm.initialize(1)
    pm.run()
    while pm.cand != 126739:
        pm.initialize(1)
        pm.run()
    print(pm.get_state())
