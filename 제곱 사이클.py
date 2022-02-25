def check(N):
    return sum(list(int(i)**2 for i in N)) if (len(N) > 1) else int(N)**2
N = input()
agg_N = int(N)
for i in range(100):
    N = check(str(N))
    if (agg_N == N):
        print(i+1)
        break
if (agg_N != N):
    print("100개 이상")
