check = 0
while True:
    while True:
        n = input()
        if n == 'exit':
            check = 1
            break
        N = int(n)
        if N == 0:
            print(0,'(0)')
            break
        elif N == 1:
            print(1,'(0)')
        elif N > 0 and N != 1:
            break
    if check == 1:
        break
    main = 0
    for i in range(N):
        if (N ** 0.5) - int(N ** 0.5) > 0:
            break
        if (N ** 0.5) - int(N ** 0.5) <= 0:
            main += 1
            N = int(N ** 0.5)

    print(N,'({0})'.format(main))


    
