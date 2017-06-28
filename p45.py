# 45
import itertools

class Solve(object):
    def __init__(self):
        self.pen_start_idx = 1
        self.hex_start_idx = 1

    def tri(self, n):
        """
        Return nth triangle numbers
        """
        return n*(n+1)/2

    def find_pen(self, target):
        """
        Find target in pentagonal numbers
        """
        for n in itertools.count(start=self.pen_start_idx):
            value = n*(3*n-1)/2
            if value > target:
                self.pen_start_idx = n
                return False
            if value == target:
                self.pen_start_idx = n + 1
                return True

    def find_hex(self, target):
        """
        Find target in hexagonal numbers
        """
        for n in itertools.count(start=self.hex_start_idx):
            value = n*(2*n-1)
            if value > target:
                self.hex_start_idx = n
                return False
            if value == target:
                self.hex_start_idx = n + 1
                return True

    def solve(self):
        for n in itertools.count(start=286):
            target = self.tri(n)
            if self.find_pen(target) and self.find_hex(target):
                return target


s = Solve()
print s.solve()