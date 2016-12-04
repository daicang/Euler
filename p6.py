# difference between sum of squares of the first 100 natural numbers and the square of the sum
import math

def solve(n):
    return math.pow(sum(range(n+1)), 2) - sum([x ** 2 for x in range(n+1)])


print solve(100)
