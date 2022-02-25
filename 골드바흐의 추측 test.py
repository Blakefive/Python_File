while(True):
    N = int(input("n = "))
    if N != 2 and N%2 == 0:
        break
chk = True
Nlist = list()
def Main(chk, N):
    test = list()
    if N != 1 and N != 2:
        for i in range(1, N+1):
            if N % i == 0:
                chk = False
                test.append(i)
        if len(test) == 2 and i != 1:
            return True
    if N == 2:
        return True

for i in range(N):
    for j in range(N):
        if i + j == N:
            if Main(chk, i) == True and Main(chk, j) == True:
                Nlist.append([i, j])
for i in range(int(len(Nlist)/2)):
    for j in range(int(len(Nlist)/2), len(Nlist)):
        if i != j:

            if Nlist[i][0] == Nlist[j][1] and Nlist[i][1] == Nlist[j][0]:
                Nlist.pop(j)

print(Nlist)
