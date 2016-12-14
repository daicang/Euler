# Find a*b, for |a|, |b| in range(1000), s.t. x^2 + a*x + b
# produces maxium number of primes for consecutive values of n


def prime_under(n):
    primes = [2]
    for x in range(3, n):
        for p in primes:
            if p * p > x:
                primes.append(x)
                break
            if x % p == 0:
                break

    return primes


def is_prime(x, primes):
    for p in primes:
        if p == x:
            return True
        elif p > x:
            return False


def solve():
    primes_b = prime_under(1000)
    primes_result = prime_under(998*998+999*998+999)
    counter_max = 0

    for b in primes_b:
        # increament: 2n + a + 1, n in [0, b-2]
        for a in range(-b+2, 1000, 2):
            counter = 1
            p = b
            for n in range(0, b):
                p += 2*n + a + 1
                if not is_prime(p, primes_result):
                    break
                counter += 1

            if counter > counter_max:
                print counter, a, b
                counter_max = counter
                result_a, result_b = a, b

    return abs(result_a*result_b)


print solve()
