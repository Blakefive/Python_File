N = input().split(",")
okcheck = len(N)-1
while(okcheck >= 0):
    final = 0
    incheck = 0
    for i in range(len(N)):
        if int(str(final)[0]) < int(N[i][0]):
            final = int(N[i])
            incheck = i
        elif int(str(final)[0]) == int(N[i][0]):
            if len(str(final)) != len(N[i]):
                max1 = len(str(final)) if len(str(final)) > len(N[i]) else len(N[1])
                for j in range(max1):
                    if j < max1-1:
                        if int(str(final)[j]) < int(N[i][j]):
                            final = int(N[i])
                            incheck = i
                            break
                    elif j >= max1-1:
                        if len(str(final)) > len(N[i]):
                            if int(str(final)[j]) < int(N[i][j-(max1-1)]):
                                final = int(N[i])
                                incheck = i
                        elif len(str(final)) < len(N[i]):
                            if int(str(final)[j-(max1-1)]) < int(N[i][j]):
                                final = int(N[i])
                                incheck = i
            elif len(str(final)) == len(N[i]):
                for j in range(len(str(final))):
                    if int(str(final)[j]) < int(N[i][j]):
                        final = int(N[i])
                        incheck = i
        
    print(final,end="")
    N.pop(incheck)
    okcheck-=1
        
        
