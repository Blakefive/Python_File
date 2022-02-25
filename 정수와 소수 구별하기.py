def main(N):
    if N - int(N) == 0:
        print("정수")
    if N - int(N) != 0:
        print("소수")
try:
    N = input()
    N = float(N)
    main(N)
except ValueError:
    print("math error")
