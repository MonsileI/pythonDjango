import random
import time

w = ["dog","snake","rabbit","pig","elephant","panda","frog"]


n = 1

print("[타자 게임] 준비되면 엔터!")
input()
start = time.time()

q=random.choice(w)
while n <= 5:
    print("*문제 no. ", n , "번")
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n = n+1
        q = random.choice(w)
    else:
        print("실패!")    


end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간 :" , et , "초")