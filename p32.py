# pandigital products


def is_pandigital(a, b, c):
    def checker(x):
        while x > 0:
            if x % 10 == 0 or arr[x % 10] == 1:
                return False
            arr[x % 10] = 1
            x /= 10
        return True

    arr = [0] * 10
    if not (checker(a) and checker(b) and checker(c)):
        return False
    for i in arr[1:]:
        if i != 1:
            return False
    return True


def solve():
    products = set()
    for a in xrange(1, 10):
        for b in xrange(1234, 9999):
            if is_pandigital(a, b, a*b):
                print a, b, a*b
                products.add(a*b)

    for a in xrange(12, 98+1):
        for b in xrange(123, 987+1):
            if is_pandigital(a, b, a*b):
                print a, b, a*b
                products.add(a*b)

    return sum(products)


print solve()
