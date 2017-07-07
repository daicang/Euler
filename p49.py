# 49
from collections import defaultdict

from prime import prime


class Solve(object):
    def __init__(self):
        self.pdict = defaultdict(list)
        self.primes = list(prime.primes_between(end=10000))

    def solve(self):
        def find_eq_diff_subseq(l):
            if len(l) < 3:
                return False

            subseqs = []
            for first_idx, first in enumerate(l):
                for second in l[first_idx+1:]:
                    eq_diff_seq = [first, second]
                    delta = second - first
                    nxt = second + delta

                    while nxt in l:
                        eq_diff_seq.append(nxt)
                        nxt += delta
                    if len(eq_diff_seq) >= 3:
                        subseqs.append(eq_diff_seq)
            return subseqs

        for p in self.primes:
            if p > 1000:
                key = ''.join(sorted(str(p)))
                self.pdict[key].append(p)

        for k, value in self.pdict.iteritems():
            eq_diff_prime = find_eq_diff_subseq(value)
            if eq_diff_prime:
                print eq_diff_prime


s = Solve()
s.solve()
