# Starting number under 1 million which produces the longest lollatz chain


def solve(n):
    l, l_idx = 0, 0
    d = {1: 1}
    for i in range(1, n+1):
        curr = i
        counter = 0
        while curr not in d:
            if curr % 2 == 0:
                curr /= 2
            else:
                curr = 3 * curr + 1
            counter += 1
        d[i] = counter + d[curr]
        if d[i] > l:
            l = d[i]
            l_idx = i

    return l_idx, l


print solve(1000000)
