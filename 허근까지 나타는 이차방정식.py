import math
Nlist = list(map(int,input().split()))
icheck = 1 if (Nlist[1]**2 - 4*Nlist[0] * Nlist[2]<0) else 0
N1 = -Nlist[1]/2 if (Nlist[1]%2 == 0) else -Nlist[1]
N2 = math.sqrt(abs((Nlist[1]/2)**2 - (Nlist[0]*Nlist[2]))) if (Nlist[1]%2 == 0) else math.sqrt(abs((Nlist[1]**2) - (4*Nlist[0]*Nlist[2])))
if (icheck == 0):
    print(N1+N2,'\n',N1-N2) if (N1+N2 != N1-N2) else print(N1+N2)
else:
    print(f"{N1} + {N2} i")
    print(f"{N1} - {N2} i")
