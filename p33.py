# digit cancelling fractions


def solve():
    def f(a, b):
        a0, a1 = a / 10, a % 10
        b0, b1 = b / 10, b % 10
        if a1 * b1 == 0:
            return False, 0, 0
        if a0 == b1:
            return True, a1, b0
        if a1 == b0:
            return True, a0, b1
        return False, 0, 0

    result = []
    for a in range(11, 100):
        for b in range(11, a):
            stat, ar, br = f(a, b)
            if stat and float(ar) / br == float(a) / b:
                result.append((a, b))
    return reduce(lambda a, b: a*b, [x[0] for x in result]), reduce(lambda a, b: a*b, [x[1] for x in result])


print solve()
