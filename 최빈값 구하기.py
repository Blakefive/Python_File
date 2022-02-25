N = list(map(int,input().split()))
M = {}
test = list()
for i in N:
    check = 0
    go = 0
    for j in range(len(test)):
        if test[j] == i:
            check = 1
            go = j
    if check == 0:
        M[i] = 1
        test.append(i)
    elif check == 1:
        M[test[go]] = M[test[go]] + 1

finalcheck = 0
usecheck = 0
for i in sorted(M.items(), key=lambda x: x[1], reverse=True):
    if usecheck != 0:
        if usecheck != list(i)[1]:
            break
    elif usecheck == 0:
        if list(i)[1] == 1:
            finalcheck = 1
            break
    usecheck = list(i)[1]
    print(str(list(i)[0]) + ' ', end='')
if finalcheck == 1:
    print("없다")
