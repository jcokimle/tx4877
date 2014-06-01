from random import randrange


class MillerRabin(object):

    def __init__(self, n=0, k=10):
        self.initialize(n, k)

    def initialize(self, n, k):
        self.log_msg = ""
        self.n = n
        self.k = k
        self.a = 0
        self.x = 0
        self.it = k
        self.cpt = 1
        self.is_prime = False
        self.is_over = False
        self.r, self.s = 0, self.n - 1
        self.step_by_step = False
        self.log("Running Miller Rabin: N = %d, K = %d" % (self.n, self.k))
        if n < 2 or n % 2 == 0:
            self.is_over = True
            self.log("N < 2 or N even => Not Prime")
            return
        if n < 6:
            self.is_over = True
            self.is_prime = [False, False, True, True, False, True][n]
            if self.is_prime:
                self.log("Prime")
            else:
                self.log("Not Prime")
            return
        while self.s % 2 == 0:
            self.r += 1
            self.s //= 2

    def run(self):
        while not self.is_over:
            self.step()
        

    def step(self):
        if not self.step_by_step and not self.is_over:
            self.step_by_step = True
        if self.it and not self.is_over:
            offset = 4
            self.log("Iteration %d" % (self.cpt), offset)
            self.it -= 1
            self.cpt += 1
            self.a = randrange(2, self.n - 1)
            self.x = pow(self.a, self.s, self.n)
            self.log("A = %d, X = %d" % (self.a, self.x), offset)
            if self.x == 1 or self.x == self.n - 1:
                self.log("X = 1 or X = N - 1 => Return", offset)
                return
            if self.r - 1 > 0:
                self.log("Starting for loop", offset)
            for _ in range(self.r - 1):
                self.x = pow(self.x, 2, self.n)
                self.log("X^2 mod N=%d" % (self.x), offset * 2)
                if self.x == 1:
                    self.log("X = 1 => Prime", offset)
                    self.is_over = True
                    self.step_by_step = False
                    return
                if self.x == self.n - 1:
                    self.log("X = N - 1 => Keep going", offset)
                    self.a = 0
                    return
            if self.a:
                self.log("A != 0 => Not Prime")
                self.is_over = True
                self.step_by_step = False
        elif not self.it and not self.is_over:
            self.log("End of iterations => Prime")
            self.is_over = True
            self.is_prime = True
            self.step_by_step = False

    def log(self, msg, offset=0):
        for _ in range(offset):
            self.log_msg = self.log_msg + " "
        self.log_msg = self.log_msg + msg + "\n"

    def get_state(self):
        return "It: %d - N: %d - K: %d - A: %d - X: %d - S: %d - R: %d - Is Prime: %d - Is Over: %d" % (self.it, self.n, self.k, self.a, self.x, self.s, self.r, self.is_prime, self.is_over)

if __name__ == "__main__":
    mr = MillerRabin()
    mr.initialize(4037391011150378392273634800292119677851, 100)
    mr.run()
    print(mr.get_state())
