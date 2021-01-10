import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)

loc = turtle.Turtle()
loc.speed(0)
loc.shape("square")
loc.color("white")
loc.penup()
loc.goto(0, 0)

txt = turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(-600, 300)
txt.write("Heyy")

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

