N = list();
while True:
    input_data = input()
    if input_data == '':
        break
    else:
        M = list(input_data)
        for i in M:
            N.append(i)
final = 0
for i in N:
    if i != ' ':
        final +=1
print(final)
