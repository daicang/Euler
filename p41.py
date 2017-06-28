# p41.py
from prime import is_prime, primes_between
from permutation import permutation


def list_to_int(l):
    if not l:
        return 0
    s = 0
    for curr in l:
        s *= 10
        s += curr
    return s


class Solve(object):
    def __init__(self):
        # prime only ends with 1/3/7 here.
        self.candidates = [list_to_int(x + [7]) for x in permutation([1, 2, 3, 4, 5, 6])]
        self.candidates.extend([list_to_int(x + [3]) for x in permutation([1, 2, 4, 5, 6, 7])])
        self.candidates.extend([list_to_int(x + [1]) for x in permutation([2, 3, 4, 5, 6, 7])])

    def solve(self):
        primes = [x for x in self.candidates if is_prime(x, primes=primes_between(end=7654321))]
        return max(primes)



s = Solve()
print s.solve()