from random import randrange


class MillerRabin(object):

    def __init__(self, n=0, k=10):
        self.initialize(n, k)

    def initialize(self, n, k):
        self.n = n
        self.k = k
        self.a = 0
        self.x = 0
        self.it = k
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
            self.it -= 1
            if self.n % 2 == 0:
                self.is_over = True
                return
            self.a = randrange(2, self.n - 1)
            self.x = pow(self.a, self.s, self.n)
            if self.x == 1 or self.x == self.n - 1:
                return
            for _ in range(self.r - 1):
                self.x = pow(self.x, 2, self.n)
                if self.x == 1:
                    self.is_over = True
                    return
                if self.x == self.n - 1:
                    self.a = 0
                    return
            if self.a:
                self.is_over = True
        elif not self.it and not self.is_over:
            self.is_over = True
            self.is_prime = True

    def get_state(self):
        return "It: %d - N: %d - K: %d - A: %d - X: %d - S: %d - R: %d - Is Prime: %d - Is Over: %d" % (self.it, self.n, self.k, self.a, self.x, self.s, self.r, self.is_prime, self.is_over)

if __name__ == "__main__":
    mr = MillerRabin()
    mr.initialize(4037391011150378392273634800292119677851, 100)
    mr.run()
    print(mr.get_state())
