Nlist = ['이유덕','이재영','권종표','이재영','박민호','강상희','이재영','김지완','최승혁','이성연','박영서','박민호','전경헌','송정환','김재성','이유덕','전경헌']
Na1,Na2,Na3 = 0,0,0
Nset = set(Nlist)
Nfinish  = list(Nset)
Nfinish.sort()
for i in range(len(Nlist)):
    if Nlist[i][0] == "김":
        Na1 += 1
    if Nlist[i][0] == "이":
        Na2 += 1
    if Nlist[i] == "이재영":
        Na3 += 1
print(f'1.김씨는 {Na1}명이고 이씨는 {Na2}명이다.')
print(f'2.이재영은 {Na3}번 반복된다.')
print(f'3.{Nset}')
print(f'4.{Nfinish}')
