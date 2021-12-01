import random

randomInt = random.randint(1,30)

while(True):
    answer = int(input("숫자를 맞혀보세요"))
    if randomInt==answer:
        print("정답입니다!")
        break
    elif randomInt > answer:
        print("조금 작은데예")
    elif randomInt < answer:
        print("조금 큰데예")    