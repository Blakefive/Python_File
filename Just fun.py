N = list(map(int,input().split()))
firstdata = N[0] - N[1]
check = 0
for i in range(len(N)-1):
    if N[i] - N[i+1] != firstdata:
        check = 1
        break
if check == 1:
    print("안 맞음")
else:
    print("맞음")
