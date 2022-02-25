N,Nformer, Nint,Nfinish = list(input()),"",1,list()
for i in range(len(N)):
    if Nformer == N[i]:
        Nint += 1
    elif Nformer != N[i]:
        if Nformer != "":
            Nfinish.append([Nformer,Nint])
            Nint = 1
    Nformer = N[i]
Nfinish.append([Nformer,Nint])
print(Nfinish)
