def main(n,m,check):
    check1 = check + 1
    Nlist = list(str(n))
    N = 0
    for i in range(len(Nlist)):
        N += int(Nlist[i])
    Nlist = list(str(N))
    list1 = list(str(n))
    if len(Nlist) == 1:
        Nlist.insert(0,list1[len(list1)-1])
    elif len(Nlist) != 1:
        Nlist[0] = list1[len(list1)-1]
    finish = ""
    for i in range(len(Nlist)):
        finish += Nlist[i]
    if int(finish) == m:
        print(check1)
        return
    elif int(finish) != m:
        main(int(finish),m,check1)

N = int(input())
main(N,N,0)

