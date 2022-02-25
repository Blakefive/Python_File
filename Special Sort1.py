def input1():
    try:
        Nlist = input().split()
        for i in range(len(Nlist)):
            Nlist[i] = int(Nlist[i])
    except ValueError:
        Nlist = input1()
    return Nlist
N, Ndecimal, Nint = input1(), list(), list()
for i in range(len(N)):
    if N[i] < 0:
        Ndecimal.append(N[i])
    if N[i] >= 0:
        Nint.append(N[i])

print(Ndecimal + Nint)
