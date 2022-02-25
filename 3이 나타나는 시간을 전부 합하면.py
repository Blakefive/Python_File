hourmin = 0
Nlist = [0,0]
def main(N,M):
    for i in range(len(str(N))):
        if str(N)[i] == '3':return 60
    for j in range(len(str(M))):
        if str(M)[j] == '3':return 60
    return 0
while True:
    Nlist[1] += 1
    if Nlist[1] == 60:
        Nlist[0] += 1
        Nlist[1] = 0
    hourmin += main(Nlist[0],Nlist[1])
    if Nlist[0] == 23 and Nlist[1] == 59:
        print(hourmin)
        break
