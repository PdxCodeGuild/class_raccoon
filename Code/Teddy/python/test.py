import turtle
turtle.setup(800,600)
board = turtle.Turtle()

def draw_face():
  board.penup()
  board.setpos(0,0)
  board.pendown()
  board.circle(100)

def draw_left_eye():
  board.penup()
  board.setpos(-50,100)
  board.pendown()
  board.circle(25)

def draw_right_eye():
  board.penup()
  board.setpos(50,100)
  board.pendown()
  board.circle(25)

def draw_right_lip():
  board.penup()
  board.setpos(0,25)
  board.pendown()
  board.circle(100,45)
  board.setheading(0)

def draw_left_lip():
  board.penup()
  board.setpos(0,25)
  board.pendown()
  board.circle(100,-45)
  board.setheading(0)

draw_face()
draw_left_eye()
draw_right_eye()
draw_left_lip()
draw_right_lip()

board.penup()
board.setpos(400,400)
turtle.done()
