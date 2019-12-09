#Drawing a stickfigure with turtle

from turtle import *
#Draw the head
circle(30)
#Draw the arms
right (45)
forward(45)
right(180)
penup()
forward(45)
pendown()
left(90)
forward(45)
left(180)
penup()
forward(45)
#Draw the body
pendown()
right(135)
forward(90)
#Draw the legs
right (45)
forward(45)
right(180)
penup()
forward(45)
pendown()
right(90)
forward(45)
done()
