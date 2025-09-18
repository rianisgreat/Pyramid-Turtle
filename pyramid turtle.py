import turtle
import random
#Sets The distance
dist = 160
#Sets the heigh
height = 0
t = turtle.Turtle()
#sets the speed
t.speed(0)
#Makes it iterate 30 times
for i in range(30):
    #Random color
    r = random.randint(0, 1)
    g = random.randint(0, 1)
    b = random.randint(0, 1)
    t.fillcolor(r,g,b)
    t.begin_fill()
    #Square
    for _ in range(4):
        t.forward(dist)
        t.right(90)
    #Changes size
    dist -= 5
    t.penup()
    t.goto(0,height)
    t.pendown()
    height+=5
    t.end_fill()

turtle.done()