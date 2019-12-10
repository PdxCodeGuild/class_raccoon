from turtle import *

# head
fillcolor("green")
begin_fill()
setposition(0,0)
circle(50)
end_fill()
right(45)

# arms
forward(100)
left(-180)
forward(100)
left(90)
forward(100)
left(-180)
forward(100)
right(135)

# body
forward(100)

# legs
right(45)
forward(100)
left(-180)
forward(100)
right(90)
forward(100)
penup()

# left eye
setposition(-25,50)
fillcolor("white")
begin_fill()
pendown()
pencolor("white")
circle(5)
end_fill()
penup()

# right eye
setposition(25,50)
fillcolor("white")
begin_fill()
pendown()
pencolor('white')
circle(5)
end_fill()
penup()

# mouth
setposition(-35,25)
pendown()
circle(50,45)
circle(45,50)

penup()
setposition(200,200)

done()
