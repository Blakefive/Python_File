def main(N):
    N = list(str(N))
    if len(N) % 2 == 0:
        for i in range(int(len(N)/2)):
            if N[i] != N[len(N)-1-i]:
                return 0
        return 1
final = 0
for x in range(100,1000):
    for j in range(100,1000):
        if final < (x*j):
            check = x * j
            if main(check) == 1:
                final = check
print(final)
