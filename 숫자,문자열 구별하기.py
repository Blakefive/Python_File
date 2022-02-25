N, Nint, Nstr,Nstrmain, Nintmain = list(input()), list(), list(), '',''
for i in range(len(N)):
    try:Nint.append(int(N[i]))
    except ValueError:Nstr.append(N[i])
for j in range(len(Nstr)):Nstrmain = Nstrmain + Nstr[j]
for j in range(len(Nint)):Nintmain = Nintmain + str(Nint[j])
print(f'str:{Nstrmain}')
print(f'int:{Nintmain}')
      
