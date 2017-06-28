# a^2 + b^2 = c^2, a + b + c = s
# => c = s - (a + b)
# a^2 + b^2 = a^2 + b^2 + 2ab + s^2 - 2sa - 2sb
# => 2s(a+b) = s^2 + 2ab


class Solve(object):
    def __init__(self):
        self.counter = [0] * 1001

    def solve(self):
        def is_int(x):
            return int(x) == x

        for a in xrange(1, 1000):
            for b in xrange(a, 1000 - a):
                c = pow(a*a + b*b, 0.5)
                if is_int(c):
                    s = a + b + c
                    if s <= 1000:
                        self.counter[int(s)] += 1

        return [x for x in xrange(1, 1001) if self.counter[x] == max(self.counter)]





s = Solve()
print s.solve()
