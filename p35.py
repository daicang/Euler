# How many circular primes are there below one million?
import math
from prime import primes_under, is_prime


class Solve(object):
    def __init__(self, bound):
        self.bound = bound
        self.primes = primes_under(math.sqrt(bound))
        self.counter = 2  # 2, 5
        self.num = [1, 3, 7, 9]

    def possible(self, x):
        while x != 0:
            if x % 10 not in self.num:
                return False
            x /= 10
        return True

    def solve(self):
        def gen_rotation(x):
            s = str(x)
            for i in xrange(len(s)):
                yield int(s[i:] + s[:i])

        for i in xrange(2, self.bound):
            if self.possible(i):
                for x in gen_rotation(i):
                    if not is_prime(x, self.primes):
                        break
                else:
                    # print i
                    self.counter += 1

        return self.counter


S = Solve(1000000)
print S.solve()
