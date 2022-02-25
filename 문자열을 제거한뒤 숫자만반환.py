N, Nintlist, Nint = list(input()), list(), ''
for i in range(len(N)):
    try:Nintlist.append(int(N[i]))
    except ValueError:pass
for i in range(len(Nintlist)):Nint += str(Nintlist[i])
print(Nint)
