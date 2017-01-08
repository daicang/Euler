# Prime lib
import math


def is_prime(x, primes):
    roof = int(math.sqrt(x))
    for p in primes:
        if p > roof:
            break
        if x % p == 0:
            return False
    return True


def primes_under(x):
    primes = []
    for i in xrange(2, int(x)+1):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes


def sum_of_divisors(x, primes):
    """
    According to: http://mathschallenge.net/library/number/sum_of_divisors
    If x = a1 * a2 * .. * ai
    Then sum_of_divisors(x) = sum_of_divisors(a1) * sum_of_divisors(a2) * ..
    For any prime p:
    sum_of_divisors(p ^ a) = ((p ^ (a + 1)) - 1) / (p - 1)

    So find all prime divisors and we can get sum of divisors.
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
