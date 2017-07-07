# Prime lib
import itertools
import math
from collections import defaultdict


class Prime(object):
    def __init__(self):
        self.primes = []

    def prime_stream(self):
        """
        Infinite prime stream
        :returns: generator, prime stream from 2

        Note: sympy.sieve is much faster
        """
        for i in itertools.count(2):
            for j in self.primes:
                if i == j:
                    yield i
                if i % j == 0:
                    break
            else:
                self.primes.append(i)
                yield i

    def is_prime(self, x, primes=None):
        """
        Prime test
        :param x: number to test
        :param primes: prime list, default: generate prime list
        :returns: bool, whether x is prime
        """
        if primes is None:
            primes = self.prime_stream()

        roof = int(math.sqrt(x))
        for p in primes:
            if p > roof:
                break
            if x % p == 0:
                return False
        return True

    def primes_between(self, start=2, end=None):
        """
        Generate primes in [start, end)
        :param start: prime start from, inclusive
        :param end: prime end, exclusive
        :returns: list of primes
        """
        stream = itertools.dropwhile(lambda x: x < start, self.prime_stream())
        if end:
            stream = itertools.takewhile(lambda x: x < end, self.prime_stream())
        return stream

    def prime_factor(self, num):
        """
        Returns prime factors
        :param num: target number
        :returns: dict of {prime-factor: power}
        """
        root = math.sqrt(num)
        factors = defaultdict(int)

        for p in self.prime_stream():
            # The only prime factor > root(num) is num itself
            # This would greatly speed up the calculation
            if p > root:
                factors[num] += 1
                break

            if num == 1:
                break

            while num % p == 0:
                factors[p] += 1
                num /= p

        return factors


def sum_of_divisors(x, primes):
    """
    According to: http://mathschallenge.net/library/number/sum_of_divisors
    If x = a1 * a2 * .. * ai, {ai} are distinctive
    Then sum_of_divisors(x) = sum_of_divisors(a1) * sum_of_divisors(a2) * ..
    For any prime p:
    sum_of_divisors(p ^ a) = ((p ^ (a + 1)) - 1) / (p - 1)

    So find all prime divisors and we can get sum of divisors.

    :param x: target number
    :param primes: prime list/stream
    :returns: sum of divisors of x
    """
    curr = x
    prime_factors = []
    for p in primes:
        if p > x:
            break
        if curr % p == 0:
            c = 0
            while curr % p == 0:
                curr /= p
                c += 1
            prime_factors.append((p, c))

    prime_factors = map(lambda x: (x[0]**(x[1]+1)-1)/(x[0]-1), prime_factors)

    return reduce(lambda x, y: x * y, prime_factors) - x

prime = Prime()