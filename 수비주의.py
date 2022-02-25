N = int(input())
check = False
def File(N):
    Nint = 0
    for i in range(1,N):
        if N % i == 0:
            Nint += i
    if N == Nint:
        print("완전수입니다")
    if N < Nint:
        print("과잉수입니다")
    if N > Nint:
        print("부족수입니다")
def File2(N):
    other1 = 0
    other2 = 0
    check = 0
    check1 = 0
    finishcheck = 0
    for i in range(1,N):
        if N % i == 0:
            other1 += i
    other2 = other1 - 1
    for i in range(1,other1):
        if other1 % i == 0:
            check += i
        if 1 < i and i <= other2-1:
            if other2 % i == 0:
                check1 += i
    if check == N:
        print(other1,"친화수입니다.")
        finishcheck = 1
    if check1 == N:
        print(other2,"혼약수입니다.")
        finishcheck = 1
    if finishcheck == 0:
        print(other1,"일반 수입니다")
    
File(N)
File2(N)
