from turtle import *

penup()
color("red")
right(90)
forward(100)
left(119)
pendown()
i=0
c="red"
while (i<100):
    forward(100)
    left(131)
    forward(60)
    left(114)
    forward(30)
    left(140)
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
