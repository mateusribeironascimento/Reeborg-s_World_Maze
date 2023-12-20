def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif right_is_clear() and wall_in_front():
        turn_right()
        move()
    elif right_is_clear() and front_is_clear():
        turn_right()
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        turn_left()
        move()