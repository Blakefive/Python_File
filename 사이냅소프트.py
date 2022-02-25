Ntemporary = input()
N = list(Ntemporary)
Nset = set(N)
for i in range(len(N)):
    if i % 2 ==0:
        N.reverse(i)
