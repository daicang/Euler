# Distinct powers
import math


def solve():
    total = 0
    l = range(2, 101)
    for x in l:
        pset = set(range(2, 101))
        for y in range(2, 101):
            z = math.pow(x, y)
            if z > 100:
                break
            for p in range(2, 101):
                # z1 = x**y1
                # z1**p1 = x**(y1*p1)
                # z2**p2 = x**(y2*p2)
                # z1**p1 == z2**p2 => y1*p1 == y2*p2
                pset.add(p*y)
            l.remove(z)
        total += len(pset)

    return total


print solve()
