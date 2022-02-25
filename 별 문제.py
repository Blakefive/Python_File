N = int(input())
n = 2 * N - 1
for i in range(n):
    if i <= N:
        for j in range(i):
            print("*", end='')
    elif i > N:
        for k in range(N - i):
            print("*", end='')
    print('')
        
