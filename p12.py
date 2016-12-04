# first triangle number to have over 500 divisors
import math


def trangles():
    curr, ret = 0, 0
    while True:
        curr += 1
        ret += curr
        yield ret


def factors(x):
    factors = 0
    s = int(math.sqrt(x))
    for i in range(1, s):
        if x % i == 0:
            factors += 2
    if x == s * s:
        factors += 1
    return factors


def solve(n):
    for t in trangles():
        if factors(t) > n:
            return t


# print factors(21), factors(28)
print solve(500)
