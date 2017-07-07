# Problem 47
# First number of first 4 consecutive numbers to have 4 distictive prime factors each
import itertools

from prime import prime


class Solve(object):
    def __init__(self):
        pass

    def solve(self):
        def satisfy(x):
            """
            Test if x has four distinctive prime factors
            """
            return len(prime.prime_factor(x)) == 4

        prev_satisfy_counter = 0
        for i in itertools.count(start=600):
            if satisfy(i):
                prev_satisfy_counter += 1
                if prev_satisfy_counter == 4:
                    return i - 3
            else:
                prev_satisfy_counter = 0


s = Solve()
print s.solve()