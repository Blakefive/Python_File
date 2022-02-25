for i in range(1,500):
    for j in range(1,500):
        k = (i**2 + j**2)**0.5
        if k - int(k) == 0:
            if i + j + k == 1000:
                print(int(i*j*k))
            break
