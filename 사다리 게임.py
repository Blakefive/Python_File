N = list(map(str, input().split()))
check = list(i for i in range(0, len(N)))
M = []
for i in range(7):
    M.append(list(map(str,list(input()))))
    for j in range(len(M[i])):
        if M[i][j] == "-":
            h = check[(j+1)//2-1]
            check[(j+1)//2-1] = check[(j+1)//2]
            check[(j+1)//2] = h
result_check = list(map(int, input().split()))
list(print(N[i], "-", result_check[int(check[i])]) for i in range(len(check)))
