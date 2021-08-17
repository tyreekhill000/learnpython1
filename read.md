def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
while not at_goal():
    pause()
    if(front_is_clear):
        move()
        if(right_is_clear):
            turn_right()
            move()