import random

count = 1
data = random.randint(1,100)
print("컴퓨터가 1~100 중 랜덤 숫자 하나를 정합니다.\n이 숫자를 맞춰주세요.")
while True:
    N = int(input("1~100 숫자 입력:"))
    if (data == N):
        break
    print("DOWN") if (N > data) else print("UP")
    count += 1
print(f"정답입니다! {count}회 만에 맞췄어요.")
