check = True
testlist = list()
while(True):
    while(True):
        N = list(map(int,input().split()))
        NM = N.pop(0)
        if NM == len(N):
            break
    if NM == 0:
        break
    for i in range(len(N)-1):
        if N[i] - N[i+1] < 0:
            testlist.append((N[i] - N[i+1])*-1)
        elif N[i] - N[i+1] >= 0:
            testlist.append(N[i]-N[i+1])
    for j in range(len(testlist)-1):
        if testlist[j] - testlist[j+1] != 1 and testlist[j] - testlist[j+1] != -1:
            check = False
    if check == True:
        print("Jolly")
    elif check == False:
        print("Not jolly")
    check = True
    testlist = list()
