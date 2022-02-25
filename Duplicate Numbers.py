Nlist,check = list(input()), True
for i in range(10):
    if Nlist.count(f'{i}') != 1:check = False
print(check)
