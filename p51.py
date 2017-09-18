# 51
# Find the smallest prime which, by replacing part of the number with the same digit,
from prime import Prime


class Solve(object):
    def __init__(self):
        self.p = Prime()
        self.ps = self.p.prime_stream()

    def get_replaced(self, p_str, r_str):
        return [int(p_str.replace(r_str, str(i))) for i in range(int(r_str), 10)]

    def solve(self):
        for p in self.ps:
            p_str = str(p)

            for num in ['0', '1', '2']:
                if p_str.count(num) > 1:
                    primes = filter(self.p.is_prime, self.get_replaced(p_str, num))
                    if len(primes) > 6:
                        print p_str, len(primes), primes
                        if len(primes) == 8:
                            return primes[0]


solver = Solve()
print solver.solve()