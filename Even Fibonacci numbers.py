Nlist= [1,2]
Nfinish = 2
check = 0
for i in range(1,4000001):
    if Nlist[check] + Nlist[check+1] == i:
        Nlist.append(i)
        check += 1
        if i % 2 == 0:
            Nfinish += i

print(Nfinish)
