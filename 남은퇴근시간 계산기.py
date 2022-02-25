N = list(map(int,input("hh:mm:ss 형식으로 입력해주세요. ").split(":")))
N.reverse()
M = [00,30,17]
final = []
check = ""
for i in range(3):
    if N[i] <= M[i]:
        if len(str(M[i]-N[i])) == 2:
            final.append(str(M[i] - N[i]))
        else:
            loop = ""
            for j in range(2-len(str(M[i]-N[i]))):
                loop += "0"
            final.append(loop+str(M[i]-N[i]))
    elif N[i] > M[i]:
        if len(str((M[i]+60)-N[i])) == 2:
            final.append(str((M[i]+60)-N[i]))
        else:
            loop = ""
            for j in range(2-str((M[i]+60)-N[i])):
                loop += "0"
            final.append(loop+str((M[i]+60)-N[i]))
        M[i+1] -= 1
final.reverse()
finalstr = ":".join(final)
print("남은 시간(hh:mm:ss) : ",finalstr)
print("남은 시간(s) : ",(int(final[0])*60 + int(final[1]))*60+int(final[2]))

