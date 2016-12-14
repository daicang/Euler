# Spiral sum


def solve(n):
    s, curr = 1, 1
    for i in range(n):
        for _ in range(4):
            curr += (i+1)*2
            s += curr

    return s


print solve((1001-1)/2)
