N = list(range(5000))
for i in range(5000):
    ok = 0
    for j in range(len(str(i))):
        ok += int(str(i)[j])
    ok += i
    try:
        N.remove(ok)
    except ValueError:
        pass
print(sum(N))
