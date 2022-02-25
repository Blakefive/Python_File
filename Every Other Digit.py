N = list(input("Example: "))
for i in range(1,len(N)):
    if i % 2 != 0:
        try:
            int(N[i])
            N[i] = '*'
        except ValueError:
            pass
finish = ""
for i in range(len(N)):
    finish += N[i]
print("→ ",finish)
