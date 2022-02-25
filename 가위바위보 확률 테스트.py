import random
test1 = 0
test2 = 0
test3 = 0
for i in range(100000000):
    m = random.randrange(1,3)
    N = random.randrange(1,3)
    if N == m:
        test1 += 1
    if N == 0:
        if m == 1:
            test2 += 1
        if m == 2:
            test3 += 1
    if N == 1:
        if m == 0:
            test3 += 1
        if m == 2:
            test2 += 1
    if N == 2:
        if m == 0:
            test2 += 1
        if m == 1:
            test3 += 1
print(test1)
print(test2)
print(test3)
