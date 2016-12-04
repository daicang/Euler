# Maxium path sum


with open('./p067-input.txt', 'r') as f:
    raw = f.read()

data = []
for l in raw.splitlines():
    data.append([int(x) for x in l.split()])


def solve():
    for i in range(len(data)-1, 0, -1):
        l1, l2 = data[i], data[i-1]
        for j in range(len(l2)):
            l2[j] += max(l1[j], l1[j+1])

    return data[0][0]


print solve()
