y_axis = 0
x_axis = 0

def go_north():
    global y_axis
    y_axis += 1
    return y_axis

def go_south():
    global y_axis
    y_axis -= 1
    return y_axis

def go_east():
    global x_axis
    x_axis += 1
    return x_axis

def go_west():
    global x_axis
    x_axis -= 1
    return x_axis


def game():
    print("You've just woken up. Confused lying the middle of a huge forest. You get up, but setting around you is not familiar"
    " at all.\nWhat other option that heading somewhere do you have? Let's hit the roud!")
    for i in range(200):
        nsew = int(input("Where do you want to go? (N - 1/S - 2/E - 3/W - 4): "))

        if nsew == 1:
            go_north()
            print("Y axis: " + str(y_axis))
            print("X axis: " + str(x_axis))
            
        elif nsew == 2:
            go_south()
            print("Y axis: " + str(y_axis))
            print("X axis: " + str(x_axis))

        elif nsew == 3:
            go_east()
            print("Y axis: " + str(y_axis))
            print("X axis: " + str(x_axis))

        elif nsew == 4:
            go_west()
            print("Y axis: " + str(y_axis))
            print("X axis: " + str(x_axis))

        else:
            print("Let's take that more seriously. Come on, input a direction.")


        if y_axis == 1 and x_axis == 1:
            print("Ou, your things. That's handy. You've got a lot of food, now you don't need to worry about it!")
        elif y_axis == -1 and x_axis == -1:
            print("Well, that was fast. You found a piece of paper with some numbers")
        elif y_axis == 12 and x_axis == 12:
            print("Uuu, a bone fire. ")
        else:
            print("There's nothing...")

    restart = input("Oh, it seems you ran out of time. Never mind, do you want to play again? (y/n): ")
    if restart == "y" or restart == "Y":
        game()


game()
