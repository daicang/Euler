# 43
from permutation import permutation
from util import list2int


class Solve(object):
    def __init__(self):
        self.s = permutation([0,1,2,3,4,5,6,7,8,9])
        self.s = [x for x in self.s if x[0] != 0]

    def f1(self, vec):
        return vec[3] % 2 == 0

    def f2(self, vec):
        return sum([vec[2], vec[3], vec[4]]) % 3 == 0

    def f3(self, vec):
        return vec[5] % 5 == 0

    def f4(self, vec):
        return list2int(vec[4:7]) % 7 == 0

    def f5(self, vec):
        return list2int(vec[5:8]) % 11 == 0

    def f6(self, vec):
        return list2int(vec[6:9]) % 13 == 0

    def f7(self, vec):
        return list2int(vec[7:10]) % 17 == 0

    def solve(self):
        def s_filter(func):
            self.s = [x for x in self.s if func(x)]

        s_filter(self.f1)
        s_filter(self.f2)
        s_filter(self.f3)
        s_filter(self.f4)
        s_filter(self.f5)
        s_filter(self.f6)
        s_filter(self.f7)

        return sum([list2int(x) for x in self.s])


s = Solve()
print s.solve()