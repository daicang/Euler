# d < 1000, 1/d contains the longest recurring cycle


def solve(n):
    def get_length(x):
        remains = []
        d = 1
        while d not in remains:
            if d == 0:
                return 0
            remains.append(d)
            d = (10 * d) % x
        return len(remains)

    x, maxlen = 0, 0
    for i in range(1, n):
        l = get_length(i)
        if l > maxlen:
            maxlen = l
            x = i
    return x, maxlen


print solve(1000)
