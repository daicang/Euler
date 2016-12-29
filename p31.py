# How many ways can euro 2 can be made?


def solve(target):
    l = [1, 2, 5, 10, 20, 50, 100, 200]

    m = []
    for i, v in enumerate(l):
        m.append([1] * (target + 1))
        for s in xrange(1, target + 1):
            if i == 0:
                m[i][s] = 1
            else:
                m[i][s] = m[i-1][s]
                s1 = s
                while s1 >= v:
                    m[i][s] += m[i-1][s1-v]
                    s1 -= v

    return m[-1][-1]


print solve(200)
