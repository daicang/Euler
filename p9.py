# solve a^2 + b^2 = c^2 which a + b + c = 1000
import math


def solve():
    for a in range(1, 1000+1):
        try:
            b = (10 ** 6 - 2 * (10 ** 3) * float(a)) / (2 * (10 ** 3) - 2 * a)
        except:
            continue
        if b <= 0:
            continue
        if int(b) == b:
            yield (a, int(b), int(1000 - a - b),
                   (1000 - a - b) == math.sqrt(a ** 2 + b ** 2))


for a, b, c, stat in solve():
    print a * b * c
