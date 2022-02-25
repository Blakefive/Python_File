Nlist = list(input())
Nint = int(input())
M = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(Nlist)):
    check = ''
    for j in range(len(M)):
        if Nlist[i] == M[j]:
            if len(M) - 1 >= (j+Nint):
                check = M[j+Nint]
            elif len(M) - 1 < (j + Nint):
                check = M[(j + Nint) -len(M)]
    print(check,end="")
