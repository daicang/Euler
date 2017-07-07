# 48

class Solve(object):
    def __init__(self):
        pass

    def solve(self, x):
        def cut(x):
            return x % 10000000000

        def pow(x, y):
            result = 1
            while y > 0:
                y -= 1
                result *= x
                cut(result)
            return result

        result = 0
        for i in range(1, x+1):
            result += pow(i, i)

        return cut(result)


s = Solve()
print s.solve(1000)