# Find the sum of all numbers which are equal to the sum of the factorial of their digits.


def calc_facs():
    result = [1]
    curr = 1
    for i in range(1, 10):
        curr *= i
        result.append(curr)
    return result


def solve():
    def fac_sum(x):
        s = 0
        while x != 0:
            s += factorials[x % 10]
            x /= 10
        return s

    nums = []
    factorials = calc_facs()
    for x in range(3, 9999999):
        if x == fac_sum(x):
            nums.append(x)

    return sum(nums)


print solve()
