#lab01_turtle.py

from turtle import *

#stick figure

#make circular head!
fillcolor('orange')
begin_fill()

# x = range(360)
# for n in x:
#     forward(1)
#     left(1)
circle(60)
end_fill()

fillcolor('oldlace')
begin_fill()
circle(50)
end_fill()


#make body
right(90)
forward(200)

#make left arm
penup()
left(180)
forward(100)
left(90)
pendown()
forward(80)
right(90)
forward(80)
left(90)
forward(25)

#move back to center
left(180)
forward(25)
right(90)
forward(80)
left(90)

#make right arm
forward(160)
right(90)
forward(80)
left(90)
forward(25)

#move back to center
left(180)
forward(25)
right(90)
forward(80)
left(90)
forward(80)
left(90)
forward(100)

#left leg
right(35)
forward(110)
right(55)
forward(30)
right(180)
forward(30)
left(55)
forward(110)

#right leg
right(110)
forward(110)
left(55)
forward(30)
left(180)
forward(30)
right(55)
forward(110)

#draw on face
penup()
right(35)
forward(260)
right(90)

#righteye
forward(10)
right(90)
pendown()
fillcolor('white')
begin_fill()
circle(10)
end_fill()
fillcolor('lightskyblue')
begin_fill()
circle(8)
end_fill()

#lefteye
penup()
right(90)
forward(40)
left(90)
pendown()
fillcolor('white')
begin_fill()
circle(10)
end_fill()
fillcolor('lightskyblue')
begin_fill()
circle(8)
end_fill()
penup()

#movetomouth
left(90)
forward(40)
right(90)
forward(26)
left(90)
forward(2)
left(90)

#drawmouth
pendown()
fillcolor('snow')
begin_fill()
circle(12, 180)
forward(10)
circle (12, 180)
forward(10)
end_fill()

penup()
left(180)
forward(4)
left(180)
pendown()
fillcolor('black')
begin_fill()
circle(12, 180)
forward(6)
circle(12, 180)
forward(6)
end_fill()

fillcolor('white')
penup()
forward(150)

done()
