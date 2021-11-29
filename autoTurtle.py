import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(200):
    a = random.randint(1,50)
    t.setheading(a)
    t.forward(10)