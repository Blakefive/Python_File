N = int(input())
m = ""
n = N
for i in range(N):
    m += "O"
while(N-1 >= 0):
    N-=1
    m = m[:N]
    for i in range(n-N):
        m += "X"
    print(m)
