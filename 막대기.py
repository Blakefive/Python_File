N = int(input())
Nlist = []
for i in range(N):
    Nlist.append(int(input()))
check = 0
final = 0
finallist = []
Nlist.reverse()
for i in range(len(Nlist)):
    if Nlist[i] > check:
        check = Nlist[i]
        final += 1
        finallist.append((len(Nlist)-i))
print(final)
