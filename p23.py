# Sum of numbers which cannot be written as 2 abundant numbers


def primes_under(x):
    primes = []
    for i in range(2, x+1):
        prime = True
        for j in primes:
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)

    return primes


def sum_of_divisors(x, primes):
    """
    According to: http://mathschallenge.net/library/number/sum_of_divisors
    If x = a1 * a2 * .. * ai
    Then sum_of_divisors(x) = sum_of_divisors(a1) * sum_of_divisors(a2) * ..
    For any prime p:
    sum_of_divisors(p ^ a) = ((p ^ (a + 1)) - 1) / (p - 1)

    So find all prime divisors and we can get sum of divisors.
    """
    curr = x
    prime_factors = []
    for p in primes:
        if p > x:
            break
        if curr % p == 0:
            c = 0
            while curr % p == 0:
                curr /= p
                c += 1
            prime_factors.append((p, c))

    prime_factors = map(lambda x: (x[0]**(x[1]+1)-1)/(x[0]-1), prime_factors)

    return reduce(lambda x, y: x * y, prime_factors) - x


def solve():
    # all numbers above 28123 can be written as the sum of 2 abundant numbers
    def is_abundant_number(x):
        return sum_of_divisors(x, primes) > x

    bound = 28123
    primes = primes_under(bound)
    abundant_numbers = [x for x in range(2, bound+1) if is_abundant_number(x)]

    as_2_ab = [False] * (bound + 1)
    for i, a in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            b = abundant_numbers[j]
            if a + b > bound:
                break
            as_2_ab[a+b] = True

    s = 0
    for i, val in enumerate(as_2_ab):
        if not val:
            s += i

    return s


print solve()
