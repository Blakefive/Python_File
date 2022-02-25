m, n = int(input('총건수:')), int(input('한페이지에 보여줄 게시물수:')) 
if m == 0:print(0)
if m != 0:
    if m >= n:print((m - n) + 1)
    if m < n:print(m)
