Ntest = input()
N = ""
Ntemporary = ""
Ntemporary1 = ""
check = 0
for i in range(1, len(Ntest)+1):
    if Ntest[i-1] == '.':
        N = Ntest[:i-1]
        Ntemporary = Ntest[i-1:]
if Ntemporary == "":
    N = Ntest
if N[0] == '-':
    Ntemporary1 = N[:1]
    N = N[1:]
check = len(N)
check1 = 0
breakint = 0
while(check > 0):
    int(N[check-1])
    check1 += 1
    if N[:check-1] != '':
        if check1 == 3:
            check1 = 0
            N = N[:check-1] + ',' + N[check-1:]
    check -= 1
print(Ntemporary1 + N + Ntemporary)
    
