import turtle
import random

dist = 160
height = 0
t = turtle.Turtle()
t.speed(0)

for i in range(30):
    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)
    t.fillcolor(r,g,b)
    t.begin_fill()
    for _ in range(4):
        t.forward(dist)
        t.right(90)
    dist -= 5
    t.penup()
    t.goto(0,height)
    t.pendown()
    height+=5
    t.end_fill()

turtle.done()