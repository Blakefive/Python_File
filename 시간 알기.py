N = input()
finishtime = 1050
Nlisttemporary = list(N)
del Nlisttemporary[2]
Nh = ''
Nm = ''
for i in range(0,2):
    Nh = Nh + Nlisttemporary[i]
for i in range(2,4):
    Nm = Nm + Nlisttemporary[i]
Nh = int(Nh)
Nm = int(Nm)
MainN = (Nh * 60)+Nm
timeremaining = finishtime - MainN
number = 0
for i in range(25):
    if timeremaining - 60 >= 0:
        timeremaining -= 60
        number += 1

print(number,':',timeremaining)

    
