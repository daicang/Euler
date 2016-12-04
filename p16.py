# sum of digits of 2 ** 1000


def solve(n):
    x = 2 ** n
    s = 0
    while x:
        s += x % 10
        x /= 10
    return s


print solve(1000)
