# Problem 46:
# Find the smallest odd composite number that cannot be written as
# the sum of a prime and twice a square.
import math
import itertools

from prime import prime

class Solve(object):
    def __init__(self):
        pass

    def solve(self):
        def is_square(n):
            root = math.sqrt(n)
            return int(root) == root

        def satisfy_goldbach(n):
            for p in prime.primes_between(start=2, end=n):
                if is_square((n-p)/2):
                    return True
            return False

        for i in itertools.ifilterfalse(prime.is_prime, itertools.count(start=9, step=2)):
            if not satisfy_goldbach(i):
                return i

s = Solve()
print s.solve()
