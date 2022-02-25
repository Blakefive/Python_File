def main(N,M,A,C,K):
    if C >= A:
        return K
    C +=1 
    C1 = A-C
    N1 = N * C
    M1 = M * C1
    if N1 > M1:
        K.append(N1)
    if N1 < M1:
        K.append(M1)
    return main(N,M,A,C,K)

mainlist = list()
N = int(input())
for i in range(N):
    Nlist = list(map(int,input().split()))
    k = list()
    mainlist.append(min(main(Nlist[0],Nlist[1],Nlist[2],0,k)))
final = ""
for i in range(len(mainlist)):
    final = final + str(mainlist[i]) +" "
print(final)
