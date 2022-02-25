
def even(N):
    return N / 2

def oddnumber(N):
    return (3*N)+1

def loop(N):
    check = N
    find = 1
    while(True):
        if check == 1:
            return find
        if check % 2 == 0:
            check = even(check)
            find += 1
        elif check % 2 == 1:
            check = oddnumber(check)
            find += 1

def main(n,m,final):
    for i in range(n,m+1):
        final.append(loop(i))
    return max(final)


N = list(map(int,input().split()))
finish = list()
print(main(N[0],N[1],finish))
