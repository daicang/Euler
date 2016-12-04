# Names scores


with open('./p022_names.txt', 'r') as f:
    content = f.read()

data = content.split(',')
data = sorted([x.strip('"') for x in data])


def val(s):
    return sum([ord(x) - ord('A') + 1 for x in s])

print sum([(i + 1) * val(x) for i, x in enumerate(data)])
