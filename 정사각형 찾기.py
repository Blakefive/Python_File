NM = list(map(int,input().split()))
while(True):
    Nlist = list()
    check = True
    Nfinish = list()
    try:
        for i in range(NM[0]):
            Nlist.append(list(str(input())))
            for j in range(NM[1]):
                Nlist[i][j] = int(Nlist[i][j])
    except IndexError:
        Nlist = list()
        check = False
    except RuntimeError:
        Nlist = list()
        check = False
    if check == True:
        break
for i in range(len(Nlist)):
    for j in range(len(Nlist[i])):
        for h in range(len(Nlist[i])):
            if j < h and (h-j)+1 > 0:
                if Nlist[i][j] == Nlist[i][h]:
                    if i+(h-j) <= len(Nlist)-1:
                        if Nlist[i+(h-j)][j] == Nlist[i+(h-j)][h]:
                            if Nlist[i][j] == Nlist[i+(h-j)][j]:
                                Nfinish.append(((h-j)+1)*((h-j)+1))

print(max(Nfinish))
