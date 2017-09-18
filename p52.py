# 52
# Find the smallest integer x, such that 2x, 3x, 4x, 5x, 6x contain the same digits.
import itertools

class Solve(object):
    def __init__(self):
        pass

    def solve(self):
        for i in itertools.count(1):
            s = set(str(i))
            for mul in [2, 3, 4, 5, 6]:
                if set(str(i * mul)) != s:
                    break
            else:
                return i


s = Solve()
print s.solve()