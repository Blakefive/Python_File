N,Nlist,Nfinish,m = list(map(int,input())),list(),"",1
for i in range(len(N)):
    try:
        Nlist.append(N[i])
        if N[i] % 2 == 0 and N[i+1] % 2 == 0:
            Nlist.insert(i+m,'*')
            m += 1
        if N[i] % 2 ==1 and N[i+1] % 2 == 1:
            Nlist.insert(i+m,'-')
            m += 1
    except IndexError:
        break
print(Nlist)
