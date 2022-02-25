inputN = input()
N = int(inputN[len(inputN)-1])
if N == 1:
    print(inputN + 'st')
elif N == 2:
    print(inputN + 'nd')
elif N == 3:
    print(inputN + 'rd')
else:
    print(inputN + 'th')
