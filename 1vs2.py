t = int(input())
N = list(map(int,input().split()))
M = list(map(int,input().split()))
check = -1
for i in range(t):
    if int(N[i]) > int(M[i]):
        check = 0
        break
    elif int(N[i]) < int(M[i]):
        check = 1
        break
    else:
        check = 2
if check == 0:
    print('win 1p')
elif check == 1:
    print('win 2p')
elif check == 2:
    print('drow')
