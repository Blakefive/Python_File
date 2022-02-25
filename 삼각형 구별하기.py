while(True):
    N = input().split()
    if len(N) == 3:break
check = 0
for i in range(len(N)):N[i] = int(N[i])
for i in range(len(N)):
    if N[i] == 0 or sum(N) != 180:
        check = 0
        break
    elif N[i] == 90:
        check = 1
        break
    elif N[i] > 90:
        check = 2
        break
    elif N[i] < 90:
        check = 3

if check == 0:print('삼각형이 아니다')
if check == 1:print('직각삼각형')
if check == 2:print('둔각삼각형')
if check == 3:print('예각삼각형')
