# d and d
print("Welcome to Dungeons and Dragons simulator!")
option1 = int(input("Do you want to play? (1/0): "))


def game_p1():
    # when user want to play
    if option1 == 1:
        print("\nYou're sitting in a noisy watering hole. You've just woken up, confused."
              "\nYou don't remember anything...")
        option2 = int(input("\nYou have three options...\n1) Get up and get out of the watering hole.\n2) Get up"
                            " and look around the watering hole.\n3) Continue sitting and looking to the void."
                            "\nWhat do you do? (1/2/3): "))
        # get outside of the pub
        if option2 == 1:
            print("You are outside the pub. It's raining. You look around. Nothing. You are in the middle of nowhere."
                  " You are standing on the side of the road, big road.\nOn the left, in the distance you see a glow."
                  " On the right you see just darkness and great mountains.")
            option3 = int(input("Where do you want to go? (left = 1/right = 0): "))
            # want to go left
            if option3 == 1:
                print("You headed for the light.")
                print("Road is longer than it seemed to be... After quite a few moments of walking, "
                      "you see a light in the forest next to you ")
            # want to go right
            elif option3 == 0:
                print("You headed for the dark.")
        # look around the pub
        elif option2 == 2:
            print("The pub seems comparatively new though it does not look luxurious. It's full of people."
                  " Odd-looking people. They are so... not open to conversation, you think.")
            option4 = int(input("Do you want to start a conversation? (1/0): "))
            # want to start conversation
            if option4 == 1:
                print("\nNow you have to choose who do you want to talk to.\nYou have three options..."
                      "\n1) Obviously drunk guy."
                      "\n2) Man sitting alone in the corner of the pub."
                      "\n3) Herd of tough guys in the middle.")
                # option5 = int(input("Who do you want to talk to? (1/2/3): "))
                # if option5 == 1:

                # elif option5 == 2:

                # elif option5 == 3:
            # don't want to start conversation
            elif option4 == 0:
                print("You are outside the pub. It's raining. You look around. Nothing. "
                      "You are in the middle of nowhere. You are standing on the side of the road, big road.\n"
                      "On the left, in the distance you see a glow. On the right you see just darkness and "
                      "great mountains.")
                option6 = int(input("Where do you want to go? (left = 1/ right = 0): "))
                # want to go left (same story as in option2)
                if option6 == 1:
                    print("You headed for the light.")
                    print("Road is longer than it seemed to be... After quite a few moments of walking, "
                          "you see a light in the forest next to you ")
                # want to go right
                elif option6 == 0:
                    print("You headed for the dark.")
        # stay sitting
        elif option2 == 3:
            print("You are sitting on a wooden bench, doing nothing. After a little while, you start to"
                  " recall snippets of information.")
            # option5 = ("")


# def game_p2():

game_p1()
# game_p2()
