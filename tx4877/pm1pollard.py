from fractions import gcd
from math import log
from random import randint
import time

from tx4877.utils import primes


class Pm1Pollard(object):

    def __init__(self, n=0, b=0, it=10):
        self.initialize(n, b, it)

    def initialize(self, n, b, it):
        '''
        Initializes the variables
        '''
        self.log_msg = ""
        self.n = n
        self.b = b
        self.it = it
        self.cpt = 1
        self.a = 0
        self.g = 0
        self.is_over = False
        self.step_by_step = False
        self.log("Running Pm1 Pollard: N = %d, B = %d, it = %d" % (self.n, self.b, self.it))

    def run(self):
        '''
        Iterates until the end of the algorithm
        '''
        while not self.is_over:
            self.step()

    def step(self):
        '''
        Computes only 1 iteration
        Adds logs at each step
        '''
        if not self.step_by_step and not self.is_over:
            self.step_by_step = True
            self.start_time = time.time()
        if self.it and not self.is_over:
            offset = 10
            self.log("Iteration %d" % (self.cpt), offset)
            self.cpt += 1
            self.it -=1
            n = self.n
            b = self.b
            self.a = randint(1, n)
            self.log("Random A between 1 and %d: A = %d" % (self.n, self.a), offset * 2)
            b_primes = primes(b)
            self.log("B = %d, computing B- primes: %s" % (self.b, b_primes), offset * 2)
            if len(b_primes) > 0:
                self.log("Start for loop", offset * 2)
            for q in b_primes :
                self.log("Q = %d" %(q), offset * 3) 
                e = abs((log(b)) / (log(q)))
                self.log("Ln(b) / Ln(q): E = %d" % (e), offset * 3)
                self.a = pow(self.a, int(pow(q, e)), n)
                self.log("Modular exponentiation A ^ Q ^ E %% N: A = %d" % (self.a), offset * 3)
            self.g = gcd(self.a - 1, n)
            self.log("Greatest Common Divisor between %d and %d: G = %d" % (self.a - 1, self.n, self.g), offset * 2)
            if 1 < self.g < n:
                self.is_over = True
                self.step_by_step = False
                self.log("Successful factorization: %d" % (self.g))
                self.log("Duration: %fs" % (time.time() - self.start_time))
            if self.g == 1 :
                self.b += 1
                self.log("G = 1 => Incrementing B and changing A", offset * 2)
        elif not self.it and not self.is_over:
            self.is_over = True
            self.step_by_step = False
            self.log("End of iterations, factorization failed")
            self.log("Duration: %fs" % (time.time() - self.start_time))

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
        return "It: %d - N: %d - B: %d - A: %d - G: %d - Is Over: %d" % (self.it, self.n, self.b, self.a, self.g, self.is_over)

''' Testing the algorithm '''
if __name__ == "__main__":
    pm = Pm1Pollard()
    pm.initialize(4037391011150378392273634800292119677851, 1, 100000)
    pm.run()
    print(pm.get_state())
