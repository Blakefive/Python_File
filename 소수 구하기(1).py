def check(N):
    check = 0
    for i in range(1,N):
        if N % i == 0:
            check +=1
    if check == 1:
        return 1
    else:
        return 0
count = 0
for i in range(2,1001):
    if check(i) == 1:
        count += 1
print(count)
