
sum = 0
bound = 4000000


def fibo_gen():
    a1, a2 = 1, 1
    while True:
        a3 = a1 + a2
        yield a3
        a1, a2 = a2, a3

for x in fibo_gen():
    if x > bound:
        break
    if x % 2 == 0:
        sum += x

print sum
