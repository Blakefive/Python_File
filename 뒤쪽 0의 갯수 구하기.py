Ninput = int(input())
N = 1
for i in range(1,Ninput+1):
    N *= i
strN = str(N)
lenN = len(strN)
finish = 0
while(lenN > 1):
    lenN -= 1
    if strN[lenN] != '0':
        break
    if strN[lenN] == '0':
        finish += 1
print(finish)
