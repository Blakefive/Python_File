Nlist, Ndecimal, Nint = input().split(), list(), list()
for i in range(len(Nlist)):
    if int(Nlist[i]) < 0:Ndecimal.append(int(Nlist[i]))
    if int(Nlist[i]) >= 0:Nint.append(int(Nlist[i]))
print(Ndecimal + Nint)
