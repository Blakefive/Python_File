N = input()
openclosecheck = 0
opencheck = list()
check = 0
for i in range(len(N)):
    if N[i] == '(':
        openclosecheck += 1
        opencheck.append(1)
    if N[i] == ')':
        openclosecheck -= 1
        if len(opencheck) == 0 == 0:
            print("not balanced")
            check = 1
            break
        else:
            opencheck.pop(0)
           

if openclosecheck != 0 and check == 0:
    print("not balanced")
if openclosecheck == 0 and check == 0:
    print("balanced")
