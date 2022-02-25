Nfinish, Nlist, Nmain = 0, list(), 1
for i in range(10,1001):
    Nlist = list(str(i))
    for j in range(len(Nlist)):
        Nmain = Nmain * int(Nlist[j])
    Nfinish += Nmain
    Nmain = 1
print(Nfinish)
