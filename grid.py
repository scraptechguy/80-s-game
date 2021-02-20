import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)
wn.tracer(0)

pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()

pen.penup()
pen.goto(0, -275)
pen.pendown()
pen.forward(25)
