N = list(map(int,input().split()))
N.sort()
if len(N) % 2 == 0:
    print(int((N[int(len(N)/2)-1] + N[int(len(N)/2)])/2))
elif len(N) % 2 == 1:
    print(N[int(len(N)/2)])
