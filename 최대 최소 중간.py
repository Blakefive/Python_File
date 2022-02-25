N = list(map(int,input().split()))
print("Max:",max(N))
print("Min:",min(N))
print("Middle:",N[int((len(N)-1)/2)] if len(N) % 2 == 1 else (N[int((len(N)/2)-1)] + N[int(len(N)/2)])/2)
