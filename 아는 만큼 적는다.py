N = list(map(int, input().split()))
for i in range(len(N)):
    if i+1 == 1 or i + 1 == 4 or i + 1 == 7:
        print(N[i])
