from turtle import * 

#variables
full_segment= 100
half_segment= 50
full_turn = 90
turn_around = 180
acute = 25
leg = half_segment + (half_segment/2)


#stick_figure_code
def head():
    fillcolor('red')
    begin_fill()

    i = 0 
    while i < 4:
        forward(full_segment)
        left(full_turn)
        i += 1
    
    forward(half_segment)

    end_fill()


def neck():
    right(full_turn)
    forward(half_segment)

def right_arm():
    right(acute + full_turn)
    forward(half_segment)
    right(turn_around)
    forward(half_segment)

def left_arm():
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
right_arm()
left_arm()
torso()
left_leg()
right_leg()

done()

#testing credential.helper store