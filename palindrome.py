def all(N):
    k = ""
    for i in range(len(N)):
        k += N[i]
    return int(k)
def main(N):
    m = ""
    N = list(str(N))
    if len(N) % 2 == 0:
        for h in range(int(len(N)/2)):
            m = N.pop(h) + m
    elif len(N) % 2 == 1:
        for h in range(int(len(N)/2)):
            m = N.pop(h) + m
        N.pop(0)
    if int(m) == all(N):
        return 1
    else:
        return 0
final = 0
for i in range(100,1000):
    for j in range(100,1000):
        if final < (i * j):
            check = i*j
            if main(check) == 1:
                final = check
print(final)
