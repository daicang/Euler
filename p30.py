# Sum of fifth power number
import math


def solve():
    def pow_sum(x):
        s = 0
        while x:
            s += d[x % 10]
            x /= 10
        return s

    result = []
    d = {x: math.pow(x, 5) for x in range(10)}
    upper_bound = int(math.pow(10, 7))
    for x in xrange(10, upper_bound):
        if pow_sum(x) == x:
            result.append(x)

    return result


r = solve()
print sum(r), r
