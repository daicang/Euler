# Lattice path through 20 * 20 grids


def solve(x0, y0):
    x, y = x0 + 1, y0 + 1
    l = [[1] * x] * y
    for i in range(1, x):
        for j in range(1, y):
            l[i][j] = l[i-1][j] + l[i][j-1]

    return l[x0][y0]


print solve(20, 20)
