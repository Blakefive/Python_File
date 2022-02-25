N = int(input())
Nfinal = ""
while True:
    if N == 1 or N == 0:
        Nfinal += str(N)
        break
    else:
        Nfinal += str(N%2)
        N = int((N-(N%2))/2)
print(Nfinal)
