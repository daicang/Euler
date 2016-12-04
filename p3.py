# largest prime factor
import math

n = 600851475143

prime_factors = []
for x in range(3, int(math.sqrt(n)), 2):
    if n % x == 0:
        n /= x
        prime_factors.append(x)

print prime_factors[-1]
