def add(N):
    M = ""
    for i in N:
        M += i
    return M

final = 0

for i in range(100, 1000):
    N = list(str(i))
    N.reverse()
    N = add(N)
    check = list(str(i * int(N)))
    test = 0
    for j in range(len(check)-1):
        if int(check[j]) > int(check[j+1]):
            test = 1
    if test == 0:
        print(check)
        final += 1
print(final)
