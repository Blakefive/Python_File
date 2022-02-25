N = int(input())
main = []
for i in range(1,N+1):
    if N % i == 0:
        main.append(i)
        main.append(int(N/i))
    if N/i - i <= i:
        break
main.sort()
print(main)
