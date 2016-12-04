# sum of numbers of 100!


def solve(n):
    x = 1
    for i in range(1, n+1):
        x *= i
        if x % 10 == 0:
            x /= 10

    return sum([int(i) for i in str(x)])


print solve(100)
