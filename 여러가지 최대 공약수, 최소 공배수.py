N = list(map(int,input().split()))
Nlist = []
for i in range(1,max(N)):
    check = 0
    for j in N:
        if j % i == 1:
            check = 1
    if check == 0:
        Nlist.append(i)
