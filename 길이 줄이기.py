"""
total = 0

for i in range(1, int(input("N의 값을 입력하세요: "))+1, 2):
    print(f"{' + ' if i!=1 else ''}", end='')
    total += i ** 3
    print(f"{i}*{i}*{i}", end='')

#print(''.join(list(f"{' + ' if i!=1 else ''}" + f"{i}*{i}*{i}" for i in range(1, int(input("N의 값을 입력하세요: "))+1, 2))))
print(f" = {total}")
"""
"""
def print_def(n):
    print(f"{' + ' if n !=1 else ''}{n}*{n}*{n}", end='')
    return n ** 3
print(" =", sum(list(print_def(i) for i in range(1, int(input("N의 값을 입력하세요: "))+1, 2))))
"""

def print_def(n):
    print(f"{'+ ' if n !=1 else ''}{n}*{n}*{n}", end=' ')
print("=", sum(filter(None , list(print_def(i) if i % 2 == 1 else (i-1)**3 for i in range(1, int(input("N의 값을 입력하세요: "))+2)))))
