# Sum of numbers which cannot be written as 2 abundant numbers


def sum_of_divisors(x):
    """
    According to: http://mathschallenge.net/library/number/sum_of_divisors
    If x = a1 * a2 * .. * ai
    Then sum_of_divisors(x) = sum_of_divisors(a1) * sum_of_divisors(a2) * ..
    For any prime p:
    sum_of_divisors(p ^ a) = ((p ^ (a + 1)) - 1) / (p - 1)

    So find all prime divisors and we can get sum of divisors.
    """
    


def solve():
    bound = 28123
    
