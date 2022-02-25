N = input().split('~')
final,m = 0,1
for i in range(int(N[0]), int(N[1])+1):
    for j in range(len(str(i))):m *= int(str(i)[j])
    final += m
    m = 1
print(final)
    
