Nlist,check = list(input().split()),0
N = int(Nlist.pop(0))
Nfinish = list()
for i in range(len(Nlist)):
    Nfinish.append(0)
for i in range(len(Nlist)):
    try:
        Nfinish[i+N] = Nlist[i]
    except IndexError:
        while(True):
            try:
                Nfinish[(i+N)-(len(Nfinish)*check)] = Nlist[i]
                break
            except IndexError:
                check += 1
    check = 0

print(Nfinish)

    
