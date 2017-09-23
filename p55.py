# 55
# How many Lychrel numbers are there below 10000?


class Solve(object):
    def __init__(self):
        self.nr_lychrel = 0
        self.bound = 10000

    def solve(self):
        def reverse_num(num):
            rev = 0
            while num != 0:
                rev *= 10
                rev += num % 10
                num /= 10
            return rev

        def is_palindrome(num):
            return num == reverse_num(num)

        for i in range(1, self.bound):
            for _ in range(50):
                i += reverse_num(i)
                if is_palindrome(i):
                    break
            else:
                self.nr_lychrel += 1

        return self.nr_lychrel

s = Solve()
print s.solve()