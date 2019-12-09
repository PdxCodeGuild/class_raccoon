from turtle import * 

full_segment= 100
half_segment= 50
full_turn = 90
turn_around = 180
acute = 25
reset = 180 - acute
leg = half_segment + (half_segment/2)

def head():
    forward(full_segment)
    left(full_turn)
    forward(full_segment)
    left(full_turn)
    forward(full_segment)
    left(full_turn)
    forward(full_segment)
    left(full_turn)
    forward(half_segment)


def neck():
    right(full_turn)
    forward(half_segment)
    right(acute + full_turn)
    forward(half_segment)
    right(turn_around)
    forward(half_segment)
    left(acute*2)
    forward(half_segment)
    left(turn_around)
    forward(half_segment)
    left(full_turn-acute)

def torso():
    forward(full_segment)

def left_leg():
    right(acute)
    forward(leg)
    right(turn_around)
    forward(leg)

def right_leg():
    right(turn_around - (acute*2))
    forward(leg)


head()
neck()
torso()
left_leg()
right_leg()

done()