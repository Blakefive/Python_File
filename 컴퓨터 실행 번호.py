N = int(input())
for i in range(N):
    Nlist = list(map(int,input().split()))
    a = Nlist[0]
    b = Nlist[1]
    print((a**b)%10)
