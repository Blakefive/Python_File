N = input().split()     #문장 받아오기
M = {}                  #M이라는 딕셔너리는 만들어서 확인한 단어을 key로 확인 개수를 value로 넣음
test = list()           #test = for문을  돌 때 이미 한 번 이상 확인한 단어인지 확인
for i in N:
    check = 0           #test에 같은 단어를 한 번만 넣기 위해 만든 변수
    go = 0              #무슨 단어를 key로 하는지 저장하기 위한 변수
    for j in range(len(test)):
        if test[j] == i:
            check = 1   
            go = j
    if check == 0:
        M[i] = 1
        test.append(i)  #test에 단어 넣기
    elif check == 1:
        M[test[go]] = M[test[go]] + 1   ##두 번 이상이면 M의 그 단어의 값에 1 더하기

finalcheck = 0
for i in sorted(M.items(), key=lambda x: x[1], reverse=True):
    finalcheck += 1
    if finalcheck == 11:
        break
    print(i)
    
        
    
