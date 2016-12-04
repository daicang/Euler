# smallest number evenly divisible by [1, 20]

# Matlab:
# l = 1 : 20
# l(isprime(l))


def solve(target):
    primes = {}
    for i in xrange(2, target + 1):
        for k in primes.keys():
            n = primes[k]
            while i % k == 0:
                i /= k
                n -= 1
            if n < 0:
                primes[k] += -n
        if i != 1:
            primes[i] = 1

    result = 1
    for factor, n in primes.iteritems():
        result *= factor ** n
    return result


print solve(20)
