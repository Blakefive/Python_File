N, nxlist, Check = int(input()), list(), False
def Main(n, x):
    for i in range(x):
        if n * i == x:
            Check = False
            return Check
        elif n * i != x:Check = True

for i in range(N):nxlist.append(list(input().split()))
for i in range(len(nxlist)):
    for j in range(len(nxlist[i])):nxlist[i][j] = int(nxlist[i][j])

for i in range(N):
    if Main(nxlist[i][1],nxlist[i][0]) == False:print(1)
    else:print(0)
