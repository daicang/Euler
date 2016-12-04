# the 10001th prime
import math


def solve(n):
    def is_prime(x):
        s = math.floor(math.sqrt(x))
        for i in primes:
            if i > s:
                break
            if x % i == 0:
                return False
        return True

    curr, counter = 2, 0
    primes = []

    while counter != n:
        if is_prime(curr):
            primes.append(curr)
            counter += 1
        curr += 1

    return primes[-1]


print solve(10001)
