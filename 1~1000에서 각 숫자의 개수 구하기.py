Nlist, Nlistmain = list(), list()
for i in range(1,1001):
    Ntemporary = str(i)
    for j in range(len(Ntemporary)):
        Nlist.append(Ntemporary[j])

for i in range(10):
    Nlistmain.append(Nlist.count(f'{i}'))
    print(f'{i}: {Nlist.count(f"{i}")}')
