import turtle

# defining window looks
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)


# Objects

# The square
loc = turtle.Turtle()
loc.speed(0)
loc.shape("square")
loc.color("white")
loc.penup()
loc.goto(0, 0)

# Just text
txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(-600, 300)
txt.write("Heyy", align="center", font=("Courier", 24, "normal"))




pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()

# Hash x up
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


# Hash x down
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


# Hash y left
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

# Hash y right
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






# defining and zeroing variables
y_axis = 0
x_axis = 0
coins = 0

# defining movement and number of coins
def go_north():
    y = loc.ycor()
    y += 50
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
    
def coin():
    global coins
    coins += 1
    return coins

# Keyboard binding
wn.listen()
wn.onkeypress(go_north, "w")
wn.onkeypress(go_south, "s")
wn.onkeypress(go_east, "d")
wn.onkeypress(go_west, "a")


# game function
while True:
    wn.update()


