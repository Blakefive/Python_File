N = list(input())
checklist = ['영','일','이','삼','사','오','육','칠','팔','구','십']
final = list()
for i in range(len(N)):
    m = 0
    try:
        m = int(N[i])
        final.append(m)
    except ValueError:
        check = -1
        for j in range(len(checklist)):
            if checklist[j] == N[i]:
                check = j
        if check != -1:
            final.append(check)
        elif check == -1:
            pass
for i in final:
    print(i,end = "")
print(" ",end="")
if str(final[0]) + str(final[1]) + str(final[2]) == "010":
    if len(final) == 11:
        print("true")
    else:
        print("false")
else:
    if len(final) == 11 or len(final) == 10:
        print("true")
    else:
        print("false")
