from turtle import *
speed(0)
penup()
color("red")
right(90)
forward(100)
left(181)
pendown()
i=0
c="red"
while (i<180):
    forward(80)
    left(181)
    if (c=="red"):
        c="orange"
    elif (c=="orange"):
        c="yellow"
    elif (c=="yellow"):
        c="green"
    elif (c=="green"):
        c="blue"
    elif (c=="green"):
        c="blue"
    elif (c=="blue"):
        c="purple"
    elif (c=="purple"):
        c="red"
    color(c)
    i=i+1

done()
