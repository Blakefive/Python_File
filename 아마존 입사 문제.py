N = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
main,check = [],0
for i in range(len(N)):
    if N[i][0] == 'a':
        main.append(N[i])
        check += 1
    else:
        main.insert((i - check)*2+1,N[i])
print(main)

"""
N = ["a1","a2","a3","a4","b1","b2","b3","b4"]
for i in range(int(len(N)/2)):
    print(N[i] + " " + N[i+int(len(N)/2)],end=" ")
"""
