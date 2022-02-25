import random
m = random.randrange(1,3)
while(True):
    N = input('가위,바위,보 중 하나를 고르시오:')
    if N == '가위' or N == '바위' or N == '보':
        if N == '가위':N = 0
        if N == '바위':N = 1
        if N == '보':N = 2
        break
if N == m:
    print('비겼습니다.')
if N == 0:
    if m == 1:print('패배하셨습니다','컴퓨터는 바위를 냈습니다')
    if m == 2:print('승리하셨습니다','컴퓨터는 보를 냈습니다')
if N == 1:
    if m == 0:print('승리하셨습니다','컴퓨터는 가위를 냈습니다')
    if m == 2:print('패배하셨습니다','컴퓨터는 보를 냈습니다')
if N == 2:
    if m == 0:print('패배하셨습니다','컴퓨터는 가위를 냈습니다')
    if m == 1:print('승리하셨습니다','컴퓨터는 바위를 냈습니다')
