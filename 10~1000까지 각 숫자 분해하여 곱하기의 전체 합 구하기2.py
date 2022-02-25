N,final = list(map(int, input().split('~'))),0
for i in range(N[0],N[1]+1):
    ok = 1
    for j in range(len(str(i))):
        ok *= int(str(i)[j])
    final += ok
print(final)
