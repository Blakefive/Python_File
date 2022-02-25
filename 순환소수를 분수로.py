import fractions

N = float(input())
M = int(input())
check = str(N).find(str(M))-1
print(fractions.Fraction( int(N*(10**check)) - int(N*(10**(check-1))), 10**check -(10**(check-1))))
