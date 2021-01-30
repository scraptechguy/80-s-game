import turtle

# defining screen looks
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)


# On screen objects

# The square
loc = turtle.Turtle()
loc.speed(0)
loc.shape("square")
loc.color("white")
loc.penup()
loc.goto(0, 0)

# Text-writing pen
txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(-600, 300)
txt.write(
    "Welcome! You've just woken up. Confused, lying the middle of a huge forest.",
    font=("Courier", 20, "normal"), 
)


# Coordinates (left down corner of the screen)
cor = turtle.Turtle()
cor.speed(0)
cor.color("white")
cor.penup()
cor.hideturtle()

# Number of coins (left corner of the screen)
cn = turtle.Turtle()
cn.speed(0)
cn.color("white")
cn.penup()
cn.hideturtle()

# Filling pen (fil position you've been to)
fill = turtle.Turtle()
fill.speed(0)
fill.color("white")
fill.hideturtle()


# Grid-writing pen
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()

# Grid x up (northern half of the grid)
pen.penup()
pen.goto(-625, 25)
pen.pendown()
pen.goto(625, 25)
pen.penup()
pen.goto(-625, 75)
pen.pendown()
pen.goto(625, 75)
pen.penup()
pen.goto(-625, 125)
pen.pendown()
pen.goto(625, 125)
pen.penup()
pen.goto(-625, 175)
pen.pendown()
pen.goto(625, 175)
pen.penup()
pen.goto(-625, 225)
pen.pendown()
pen.goto(625, 225)
pen.penup()
pen.goto(-625, 275)
pen.pendown()
pen.goto(625, 275)
pen.penup()


# Grid x down (southern half of the grid)
pen.penup()
pen.goto(-625, -25)
pen.pendown()
pen.goto(625, -25)
pen.penup()
pen.goto(-625, -75)
pen.pendown()
pen.goto(625, -75)
pen.penup()
pen.goto(-625, -125)
pen.pendown()
pen.goto(625, -125)
pen.penup()
pen.goto(-625, -175)
pen.pendown()
pen.goto(625, -175)
pen.penup()
pen.goto(-625, -225)
pen.pendown()
pen.goto(625, -225)
pen.penup()
pen.goto(-625, -275)
pen.pendown()
pen.goto(625, -275)
pen.penup()


# Grid y left (western half of the grid)
pen.penup()
pen.goto(-25, 275)
pen.pendown()
pen.goto(-25, -275)
pen.penup()
pen.goto(-75, 275)
pen.pendown()
pen.goto(-75, -275)
pen.penup()
pen.goto(-125, 275)
pen.pendown()
pen.goto(-125, -275)
pen.penup()
pen.goto(-175, 275)
pen.pendown()
pen.goto(-175, -275)
pen.penup()
pen.goto(-225, 275)
pen.pendown()
pen.goto(-225, -275)
pen.penup()
pen.goto(-275, 275)
pen.pendown()
pen.goto(-275, -275)
pen.penup()
pen.goto(-325, 275)
pen.pendown()
pen.goto(-325, -275)
pen.penup()
pen.goto(-375, 275)
pen.pendown()
pen.goto(-375, -275)
pen.penup()
pen.goto(-425, 275)
pen.pendown()
pen.goto(-425, -275)
pen.penup()
pen.goto(-475, 275)
pen.pendown()
pen.goto(-475, -275)
pen.penup()
pen.goto(-525, 275)
pen.pendown()
pen.goto(-525, -275)
pen.penup()
pen.goto(-575, 275)
pen.pendown()
pen.goto(-575, -275)
pen.penup()
pen.goto(-625, 275)
pen.pendown()
pen.goto(-625, -275)
pen.penup()

# Grid y right (eastern half of the grid)
pen.penup()
pen.goto(25, 275)
pen.pendown()
pen.goto(25, -275)
pen.penup()
pen.goto(75, 275)
pen.pendown()
pen.goto(75, -275)
pen.penup()
pen.goto(125, 275)
pen.pendown()
pen.goto(125, -275)
pen.penup()
pen.goto(175, 275)
pen.pendown()
pen.goto(175, -275)
pen.penup()
pen.goto(225, 275)
pen.pendown()
pen.goto(225, -275)
pen.penup()
pen.goto(275, 275)
pen.pendown()
pen.goto(275, -275)
pen.penup()
pen.goto(325, 275)
pen.pendown()
pen.goto(325, -275)
pen.penup()
pen.goto(375, 275)
pen.pendown()
pen.goto(375, -275)
pen.penup()
pen.goto(425, 275)
pen.pendown()
pen.goto(425, -275)
pen.penup()
pen.goto(475, 275)
pen.pendown()
pen.goto(475, -275)
pen.penup()
pen.goto(525, 275)
pen.pendown()
pen.goto(525, -275)
pen.penup()
pen.goto(575, 275)
pen.pendown()
pen.goto(575, -275)
pen.penup()
pen.goto(625, 275)
pen.pendown()
pen.goto(625, -275)
pen.penup()



# Defining coordinates and setting it's value to zero  
y_axis = 0
x_axis = 0

# Defining movement
def go_north():
    y = loc.ycor()
    y += 50             # Jumping by 50 pixels per click
    loc.sety(y)

def go_south():
    y = loc.ycor()
    y -= 50
    loc.sety(y)

def go_east():
    x = loc.xcor()
    x += 50
    loc.setx(x)

def go_west():
    x = loc.xcor()
    x -= 50
    loc.setx(x)


# Keyboard binding with movement functions
wn.listen()
wn.onkeypress(go_north, "w")
wn.onkeypress(go_south, "s")
wn.onkeypress(go_east, "d")
wn.onkeypress(go_west, "a")



# Square filling function (Yes, that's why all the squares are purple )
def draw():
    # Drawing a square that will be filled (The square is the same size as one grid square)
    def square():
        fill.goto(loc.xcor(), loc.ycor())       # Fill pen will follow loc object
        fill.penup()
        fill.forward(25)
        fill.right(90)
        fill.pendown()
        fill.forward(25)
        fill.right(90)
        fill.forward(50)
        fill.right(90)
        fill.forward(50)
        fill.right(90)
        fill.forward(50)
        fill.right(90)
        fill.forward(25)
        fill.penup()
        fill.right(90)
        fill.forward(25)
        fill.right(180)
        fill.penup()

    # Fill color + actual filling of the square  
    fill.fillcolor("purple")
    fill.begin_fill()
    square()
    fill.end_fill()


# Defining coin concerning variables and setting all of them equal to zero
coins = 0
# c1, c2, and c3 are places with coins. When the place is found by player for the first time, value increases by 1 ->
# -> program will be able to tell, whether you already received a coin for that certain place  
c1 = 0
c2 = 0      # Coin collecting mechanism to avoid mistakes in number of coins
c3 = 0

# Game loop
while True:
    wn.update()
    draw()

    # Displaying coordinates info (left down corner of the screen)
    cor.clear()
    cor.goto(-600, -300)
    cor.write("X: {}       Y: {}".format(loc.xcor(), loc.ycor()))

    # Displaying coins info (left down corner of the screen)
    cn.clear()
    cn.goto(-600, -320)
    cn.write("Coins: {}   ".format(coins))

    # Boarders (As soon as boarder is hit, loc is moved back by one jump, 50 pixels.)
    
    # Left side
    if loc.xcor() < -625:
        loc.setx(-600)

    # Right side
    elif loc.xcor() > 625:
        loc.setx(600)
    
    # Bottom side 
    elif loc.ycor() < -275:
        loc.sety(-250)
    
    # Top side
    elif loc.ycor() > 275:
        loc.sety(250)

    # Places with actions (If you step on certain location, something will happen.)
    if loc.xcor() == 50 and loc.ycor() == 0:
        txt.clear()
        txt.goto(-600, 300)
        txt.write( 
            "Wow that was fast, you found something. Good for you!",
            font=("Courier", 24, "normal"),
        )

    elif loc.xcor() == 100 and loc.ycor() == -100:
        txt.clear()
        txt.write(
            "Heyy",
            font=("Courier", 24, "normal")
        )


    # Places with coins 

    # c1
    elif loc.xcor() == 50 and loc.ycor() == -50:
        txt.clear()
        txt.write(
            "Next one! Great.",
            font=("Courier", 24, "normal")
        )

        # Coin collecting mechanism
        if coins == 0:
            coins = 1

        elif coins == 1 and c2 == 1:
            coins = 2

        elif coins == 1 and c3 == 1:
            coins = 2

        elif coins == 2 and c2 == 1 and c3 == 1:
            coins = 3

        c1 = 1

    # c2
    elif loc.xcor() == -50 and loc.ycor() == -50:
        txt.clear()
        txt.write(
            "Hm, something shiny's lying on the ground. Yes! It's a coin. ",
            font=("Courier", 24, "normal")
        )

        # Coin collecting mechanism
        if coins == 0:
            coins = 1

        elif coins == 1 and c1 == 1:
            coins = 2

        elif coins == 1 and c3 == 1:
            coins = 2

        elif coins == 2 and c1 == 1 and c3 == 1:
            coins = 3

        c2 = 1

    # c3
    elif loc.xcor() == -100 and loc.ycor() == -50:
        txt.clear()
        txt.write(
            "Another one! Good for you.",
            font=("Courier", 24, "normal")
        )

        # Coin collecting mechanism
        if coins == 0:
            coins = 1

        elif coins == 1 and c1 == 1:
            coins = 2

        elif coins == 1 and c2 == 1:
            coins = 2

        elif coins == 2 and c1 == 1 and c2 == 1:
            coins = 3

        c3 = 1      
