N = list(map(int,input("ax + by = c").split()))
M = list(map(int,input("dx + ey = f").split()))
if N[0] != M[0]:
    test = N[0] / M[0]
    M[0] = M[0] * test
    M[1] = M[1] * test
    M[2] = M[2] * test
if N[0] == M[0]:
    b = N[1] - M[1]
    c = N[2] - M[2]
if b != 1:
    c = c / b
    b = 1
if b < 0:
    c * -1
y = c
b = N[1] * y;c = N[2] - b;a = N[0]
if a != 1:
    c = c / a
    a = 1
x = c
print("X = ",end="")
print(format(x,'.12g'))
print("Y = ",end="")
print(format(y,'.12g'))
