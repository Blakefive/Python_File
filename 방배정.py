import math
N = list(map(int,input().split()))
Ndir = {1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0],6:[0,0]}
for i in range(N[0]):
    Nlist = list(map(int,input().split()))
    if Nlist[0] == 0:
        Ndir[Nlist[1]][0] += 1
    if Nlist[0] == 1:
        Ndir[Nlist[1]][1] += 1
final = 0  
gogo1 = 0
gogo2 = 0
for i in range(1,7):
    gogo1 += Ndir[i][0]
    gogo2 += Ndir[i][1]
    if i == 4 or i == 6:
        if gogo1 != 0:
            final += math.ceil(gogo1/N[1]) if gogo1 >= N[1] else 1
        if gogo2 != 0:
            final += math.ceil(gogo2/N[1]) if gogo2 >= N[1] else 1
        gogo1 = 0
        gogo2 = 0
    if  i == 2:
        if gogo1 != 0 or gogo2 != 0:
            final += math.ceil((gogo1+gogo2)/N[1]) if (gogo1+gogo2) >= N[1] else 1
        gogo1 = 0
        gogo2 = 0
print(final)
