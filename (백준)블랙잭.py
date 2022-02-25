_, check_n = input().split()
check = list(map(int, input().split()))
g = 0
for i in range(len(check)):
    for j in range(i+1, len(check)):
        for k in range(j+1, len(check)):
            if g < check[i]+check[j]+check[k] and int(check_n) >= check[i]+check[j]+check[k]:
                g = check[i]+check[j]+check[k]
print(g)
