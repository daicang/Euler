# 53



class Solve(object):
    def __init__(self):
        self.bound = 1000000
        self.cnt = 0

    def solve(self):
        for n in range(22, 101):
            last_cnr = 1
            for r in range(1, n/2):
                last_cnr = last_cnr * (n-r+1) / r
                if last_cnr > self.bound:
                    self.cnt += n - 1 - 2 * (r - 1)
                    break

        return self.cnt


s = Solve()
print s.solve()