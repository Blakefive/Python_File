ListMain = list()
CheckMain = False
def Main(i):
    for j in range(i):
        if len(list(str(j))) == 2:
            ListMain = (list(str(10)))
            if int(ListMain[0]) + int(ListMain[1]) + j == i:
                CheckMain = True
                return CheckMain
        elif len(list(str(j))) == 1:
            if j + 0 + j == i:
                CheckMain = True
                return CheckMain

for i in range(1,100):
    if Main(i) == True:
        ListMain.append(Main(i))
print(Main(3))
print(ListMain)

