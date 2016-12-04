# largest palidrome made from the product of 2 3-digit numbers


def is_pali(n):
    return str(n) == str(n)[::-1]


def solve():
    for a in range(800, 1001):
        for b in range(800, 1001):
            if is_pali(a * b):
                print a * b

solve()
