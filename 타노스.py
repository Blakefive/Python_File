import random

N = list(map(int,input().split()))
if len(N) % 2 != 0:
    m = random.randrange(1,2)
    if m == 1:
        for i in range(int(len(N)/2)):
            N.pop(random.randrange(1,len(N)))
    if m == 2:
        for i in range(int(len(N)/2)+1):
            N.pop(random.randrange(1,len(N)))
elif len(N) % 2 ==0:
    for i in range(int(len(N)/2)):
        N.pop(random.randrange(1,len(N)))

print(N)
