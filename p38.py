

class Solve(object):
    def __init__(self):
        self.low_bound =918273645

    def gen(self):
        def f(x):
            return len(str(x)) == len(set(str(x)))

        for i in filter(f, xrange(90, 100)):
            yield i
        for i in filter(f, xrange(900, 1000)):
            yield i
        for i in filter(f, xrange(9000, 10000)):
            yield i

    def pandigital(self, x):
        s = str(x)
        i = 1
        while len(s) < 9:
            i += 1
            s += str(x*i)
        if len(s) == 9 and '0' not in s and len(s) == len(set(s)):
            return int(s)
        return False

    def solve(self):
        p_max = self.low_bound
        for i in self.gen():
            p = self.pandigital(i)
            p_max = max(p_max, p) if p else p_max
        return p_max


s = Solve()
print s.solve()