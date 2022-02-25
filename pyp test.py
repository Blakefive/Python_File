N = 1
while True:
    check = 0
    for i in range(1,21):
        if N % i != 0:
            check = 1
        if check == 0:
            break
    N += 1
print(N)
