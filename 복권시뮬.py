import random

# BUY
num = int(input("몇 개를 사실건가요? : "))
print("{}개 구매".format(num))

# Number
c_m = list(map(int, input("번호를 입력하세요 : ").split()))
print("저장 성공")

# 출력
print("[시뮬레이션을 시작합니다.]")
print("--------------------------")

for i in range(1,num*7+1):
    x1 = random.randint(1, 45)
    print("{}".format(x1))
    if i % 7 == 0:
        print("\n")

print("-----End-----")