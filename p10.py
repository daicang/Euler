# sum of primes under 2000000
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

    primes = []
    for i in xrange(2, n+1):
        if is_prime(i):
            primes.append(i)

    return sum(primes)


print solve(2000000)
