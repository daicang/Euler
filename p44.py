# 44
import math
import itertools

class Solve(object):
    def __init__(self):
        pass

    def solve(self):
        """
        Solve: find pentagon number small, big (small < big), s.t.:
        delta = big - small (assume delta < small),
        sum = small + big are also pentagon numbers

        We loop big_x and small_x, test if:
        1. delta = big - small is pentagon
        2. sum = big + small is pentagon
        """

        def is_pentagon(y):
            """
            Calculates inverse function to test pentagon numbers,
            function: y = x(3x - 1) / 2
            inverse function: x = (root(24y + 1) + 1) / 6
            """
            x = (math.sqrt(24 * y + 1) + 1) / 6
            return int(x) == x and x

        def func(x):
            return x * (3 * x - 1) / 2

        for big_x in itertools.count(start=1):
            for small_x in range(1, big_x):
                small = func(small_x)
                big = func(big_x)
                sum = small + big
                delta = big - small

                if is_pentagon(sum) and is_pentagon(delta):
                    return delta

s = Solve()
print s.solve()