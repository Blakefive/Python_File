N = list(map(int,input().split()))
N.sort()
result = []
for i in range(len(N)):
    if (N[i] % 2 == 1):
        result.append(N[i])
    elif (len(N)%2 == 0):
        result.append(N[len(N)-i])
    else:
        result.append(N[len(N)-(i+1)])
print(result)
