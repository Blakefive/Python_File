def kaprekar_number(N):
    M = N**2
    if len(str(M)) == 1:
        if M == N:return True
        elif M != N:return False
    elif len(str(M)) % 2 == 0:
        h = int(str(M)[:int(len(str(M))/2)]) + int(str(M)[int(len(str(M))/2):])
        if h == N:return True
        elif h != N:return False
    elif len(str(M)) % 2 == 1:
        h1 = int(str(M)[:int(len(str(M))/2)]) + int(str(M)[int(len(str(M))/2):])
        h2 = int(str(M)[:int(len(str(M))/2)+1]) + int(str(M)[int(len(str(M))/2)+1:])
        if h1 == N or h2 == N:return True
        elif h1 != N and h2 != N:return False
def kaprekar_constant(N):
    p,line = 0,0
    if len(str(N)) != 4:

        p = 4 - len(str(N))
    while True:
        line += 1
        Nstr,Mstr = "",""
        Nlist,Mlist = list(str(N)),list(str(N))
        truefalsecheck = 0
        check = int(str(N)[0])
        for j in range(p):
            Nlist.append('0')
            Mlist.append('0')
        p = 0
        for i in range(len(Nlist)):
            Nlist[i] = int(Nlist[i])
        for i in range(len(str(N))):
            if int(str(N)[i]) == check:
                truefalsecheck += 1
        if truefalsecheck == len(str(N)):return False
        elif truefalsecheck != len(str(N)):
            Nlist.sort()
            Mlist.sort()
            Mlist.reverse()             
            for j in range(len(Nlist)):
                Nstr += str(Nlist[j])
                Mstr += str(Mlist[j])
            if int(Mstr) - int(Nstr) == 6174:return line
            elif int(Mstr) - int(Nstr) != 6174:
                N = int(Mstr)-int(Nstr)
print(kaprekar_number(int(input())))
print(kaprekar_constant(int(input())))
