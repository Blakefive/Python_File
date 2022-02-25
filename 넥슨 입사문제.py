N = list()
for i in range(5000):
    check = 0
    for j in range(len(str(i))):
        check += int(str(i)[j])
    check += i
    N.append(check)
final = 0
for i in range(5000):
    ok = 0
    for j in range(len(N)):
        if i == N[j]:
            ok = 1
            break
    if ok == 0:
        final += i
print(final)
