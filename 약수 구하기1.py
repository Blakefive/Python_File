N = int(input())
final = 0
print('{',end='')
for i in range(1,N+1):
    if N % i == 0:
        if i != N:
            print(str(i) + ',',end='')
        if i == N:
            print(str(i) + '}')
        final += 1
print("약수의 개수는 " + str(final) + "개 입니다.")

