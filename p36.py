# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.


class Solve(object):
    def __init__(self):
        self.bound = 1000000
        self.sum_of_palin = 0

    @staticmethod
    def is_palin_base10(x):
        s = str(x)
        return s == s[::-1]

    @staticmethod
    def is_palin_base2(x):
        if x % 2 == 0:
            return False
        l = []
        while x != 0:
            l.append(x % 2)
            x /= 2
        return l == l[::-1]

    def solve(self):
        for i in xrange(1, self.bound+1):
            if self.is_palin_base10(i) and self.is_palin_base2(i):
                self.sum_of_palin += i
        return self.sum_of_palin


s = Solve()
print s.solve()
