while True:
    n = input()
    N = int(n)
    if N > 0:
        break

def right(N):
    right = [0,1]
    mainright = []
    for r in range(len(right)):
        mainright.append(N - right[r])
    return mainright

def left(N):
    left = [1,2,3]
    mainleft = []
    for l in range(len(left)):
        mainleft.append(N - left[l])
    return mainleft

while True:
    first = right(N)
    second = left(first[0])
    for l in range(len(first)):
        for r in range(len(second)):
            if second[r] == 0:
                print(N+second[r])
                print(first[l])
        break
