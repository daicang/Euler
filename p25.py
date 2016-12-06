# Index of first Fibonacci number to have 1000 digits
import math


def solve(n):
    # Phi = (5^0.5 + 1) / 2
    # Fibo(i) = round(Phi^i/5^0.5)
    root_5 = math.pow(5, 0.5)
    i = 1
    while True:
        d = 1+math.floor(i*(math.log10(root_5+1)-math.log10(2))-math.log10(5)/2)
        if d >= n:
            break
        i += 1
    return i


print solve(1000)
