N = int(input())
Nlistfinish = list()
for h in range(N):
    Nlist = list(input().split())
    check = len(str(int(Nlist[0])**int(Nlist[1])))
    if str(int(Nlist[0])**int(Nlist[1]))[len(str(int(Nlist[0])**int(Nlist[1])))-1] != '0':
        Nlistfinish.append(str(int(Nlist[0])**int(Nlist[1]))[len(str(int(Nlist[0])**int(Nlist[1])))-1])
    if str(int(Nlist[0])**int(Nlist[1]))[len(str(int(Nlist[0])**int(Nlist[1])))-1] == '0':
        Nlistfinish.append('10')
for i in range(len(Nlistfinish)):
    print(Nlistfinish[i])
