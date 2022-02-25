import math

def isPrime(num):
    if num == 1: return False

    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k ==0: return False
    return True

while(True):
    N, M = map(int, input().split())
    if N >= 1000000000 and N <= 1000000000000 and M >= 0 and M <= 1000000:
        break

NM = N + M

for k in range(N, NM +1):
    if isPrime(k) : print(k)

