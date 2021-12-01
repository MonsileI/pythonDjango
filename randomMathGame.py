import random


while(True):
    print(" 0을 입력하시면 종료됩니다~!")
    a= random.randint(1,40)
    b= random.randint(1,40)

    print(a,"+",b,)

    answer = int(input("정답은?"))

    if(answer == a+b ):
        print("올~")
    elif(answer == 0):
        print("종료되었습니다.")
        break    
    else:
        print("stupid")
    

    