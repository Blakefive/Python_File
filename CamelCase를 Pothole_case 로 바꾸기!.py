N = list(input())
finallist = []
check = ""
for i in range(len(N)):
    if N[i] == N[i].upper():
        finallist.append(check+"_")
        check = N[i].lower()
    else:
        check += N[i]
final = ""
for j in finallist:
    final += j
print(final+check)
