N = list(map(int,input().split()))
finish = 0
for i in range(N[0]):
    if N[0] + (N[1] * i) < N[2] * i:
        print(i)
        break

