# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
import prime

class Solve(object):
    def __init__(self):
        self.such_primes = []
        self.nr_such_prime = 11

    def solve(self):
        def contain_even(x):
            for i in str(x):
                if i in '0468':
                    return True
            return False

        def gen_truncates(x):
            s = str(x)
            for i in  range(1, len(s)):
                yield int(s[:i])
            for i in range(len(s)-1, 0, -1):
                yield int(s[i:])

        primes = [2, 3, 5, 7]
        for p in prime.primes_between(start=10):
            primes.append(p)
            if not contain_even(p):
                for i in gen_truncates(p):
                    if i not in primes:
                        break
                else:
                    print len(self.such_primes), 'Found', p
                    self.such_primes.append(p)
                    if len(self.such_primes) >= self.nr_such_prime:
                        break

        return sum(self.such_primes)


s = Solve()
print s.solve()
