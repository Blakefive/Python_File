N = int(input())
Nfinish = list()
for i in range(N):
    check = 0
    finish = 0
    Nmain = list(input())
    for j in range(len(Nmain)):
        if Nmain[j] == 'O':
            check += 1
            finish += check
        if Nmain[j] == 'X':
            check = 0
    Nfinish.append(finish)
for i in range(len(Nfinish)):
    print(Nfinish[i])
