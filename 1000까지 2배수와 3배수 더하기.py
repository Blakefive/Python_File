N, a, b = 0, 0, 0
for i in range(1,1001):
    if a % i == 0:N += i
    if b % i == 0:N += i
print(N)

