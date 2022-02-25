N = int(input())
Nlist = list()
for i in range(1,N+1):
    if N%i == 0:
        Nlist.append(i)

print(Nlist)
print(f"약수의 개수는 {len(Nlist)}개 입니다")
