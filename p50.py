# 50
# Find the prime below 1000000, which can be written as sum of most consecutive primes
# 997651
from datetime import datetime
from sympy import sieve

from prime import prime


class Solve(object):
    def __init__(self):
        pass

    def solve(self):
        # primes under 1000000: 78498
        # prime.prime costs 3min 56sec
        # sympy.sieve: 0.6sec, 100x faster

        # primes = list(prime.primes_between(end=1000000))
        primes = list(sieve.primerange(2, 1000000))
        lenp = len(primes)
        csums = [0]*(lenp+1)
        max_length = 1
        result = 0

        for i in range(lenp):
            csums[i+1] = csums[i] + primes[i]

        def bisearch_prime(x, primes):
            lo, hi = 0, len(primes)

            while lo < hi:
                mid = (lo+hi)//2
                if x < primes[mid]:
                    hi = mid - 1
                elif x > primes[mid]:
                    lo = mid + 1
                else:
                    return True

            return False


        for end_idx in range(lenp+1):
            # start_idx: inclusive, end_idx: exclusive
            # 42sec
            for start_idx in reversed(range(end_idx-max_length)):
                target = csums[end_idx] - csums[start_idx]
                if target > 1000000:
                    break
                if bisearch_prime(target, primes):
                    max_length = end_idx - start_idx
                    result = target

        # for start_idx in range(lenp):
        #     # As for double-loop infinite sequence, loop end index in outer loop is better.
        #     # 40sec
        #     for end_idx in range(start_idx+max_length+1, lenp+1):
        #         target = csums[end_idx] - csums[start_idx]
        #         if target > 1000000:
        #             break
        #         if bisearch_prime(target, primes):
        #             max_length = end_idx - start_idx
        #             result = target

        return result


start = datetime.now()
s = Solve()
print s.solve()
print datetime.now() - start
