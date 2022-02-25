N,NM,JK = list(input().split(', ')), 0, 0
for i in range(len(N)):
    if int(N[i]) % 2 == 0:
        NM += 1
    if int(N[i]) % 2 == 1:
        JK += 1

print(f'홀수 {JK}개, 짝수 {NM}개')
