N, Nmain, Ncheck = 0, 0, True
while(Ncheck):
    N += 20
    for i in range(1,21):
        Nmain += N%i
    if Nmain == 0:
        Ncheck = False
    Nmain = 0
print(N)
