Nfinish = list()
Ntemporary = ""
while(True):
    Nmain = int(input())
    if Nmain >= 1 and Nmain <= 16:
        break
while(True):
    N = list(map(int,input().split(',')))
    N1 = list(map(int,input().split(',')))
    if len(N) == Nmain and len(N1) == Nmain:
        break
for i in range(Nmain):
    N[i] = bin(N[i])[2:]
    N1[i] = bin(N1[i])[2:]
for j in range(Nmain):
    Nfinish.append(int(N[j])+int(N1[j]))
    Nfinish[j] = str(Nfinish[j])
for k in range(Nmain):
    for h in range(len(Nfinish[k])):
        if int(Nfinish[k][h]) >= 1:
            Ntemporary += "#"
        else:
            Ntemporary += " "
    Nfinish[k] = Ntemporary
    Ntemporary = ""
print(Nfinish)
