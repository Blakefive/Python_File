N = list(map(int,input("ax^2 + bx + cx = 0일때 a,b,c을 작성해주세요.").split()))
M = (-N[1] + ((N[1]**2 -4*N[0]*N[2])**0.5))/(2*N[0])
M2 = (-N[1] - ((N[1]**2 -4*N[0]*N[2])**0.5))/(2*N[0])
if N[1]**2 -4*N[0]*N[2] > 0:
    print(M)
    print(M2)
if N[1]**2 - 4*N[0]*N[2] == 0:
    print(M)
if N[1]**2 - 4* N[0]*N[2] < 0:
    print("없다")
