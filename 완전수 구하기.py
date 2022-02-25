N,Nlist,Nfinishlist = int(input()), list(), list()
for i in range(1,N+1):
    for j in range(1,i):
        if i%j == 0:Nlist.append(j)
    if sum(Nlist) == i:Nfinishlist.append(i)
    Nlist = list()
print(Nfinishlist)

