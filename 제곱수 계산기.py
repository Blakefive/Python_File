def square(N):
    check = 0
    n = N
    while(True):
        if n**0.5 - int(n**0.5) == 0:
            check += 1
            n = n**0.5
        elif n**0.5 - int(n**0.5) != 1:
            return str(int(n))+"("+str(int(check))+")"

def make(N):
    n = ""
    checklist1 = list()
    checklist2 = list()
    check = 0
    mainlist = list(N)
    for i in range(len(mainlist)):
        if mainlist[i] == '(':
            check = 1
        if check == 0:
            checklist1.append(mainlist[i])
        elif check == 1:
            checklist2.append(mainlist[i])
    checklist2.pop(0)
    checklist2.pop(len(checklist2)-1)
    for j in range(len(checklist1)):
        n += checklist1[j]
    check = ""
    for k in range(len(checklist2)):
        check += checklist2[k]
    n = int(n)
    check = int(check)
    for i in range(check):
        n *= n
    return n

N =input()
try:
    N = int(N)
    print(square(N))
except ValueError:
    print(make(N))
            
