import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=1280, height=720)


blueRocket2 = turtle.Turtle()
blueRocket2.hideturtle()
blueRocket2.penup()
blueRocket2.color("blue")
blueRocket2.shape("square")
blueRocket2.shapesize(0.5, 0.5)
blueRocket2.goto(-400, -50)

blueRocket3 = turtle.Turtle()
blueRocket3.hideturtle()
blueRocket3.penup()
blueRocket3.color("blue")
blueRocket3.shape("square")
blueRocket3.shapesize(0.5, 0.5)
blueRocket3.goto(-400, -50)

blueRocket4 = turtle.Turtle()
blueRocket4.hideturtle()
blueRocket4.penup()
blueRocket4.color("blue")
blueRocket4.shape("square")
blueRocket4.shapesize(0.5, 0.5)
blueRocket4.goto(-400, -50)

blueRocket = turtle.Turtle()
blueRocket.hideturtle()
blueRocket.color("gray")
blueRocket.shape("square")
blueRocket.shapesize(0.4, 2)
blueRocket.penup()
blueRocket.goto(-400, -450)
blueRocket.showturtle()
blueRocket.left(90)
blueRocket.forward(400)
blueRocket.hideturtle()

blueRocket2.showturtle()
blueRocket3.showturtle()
blueRocket4.showturtle()


for i in range(30):
    by2 = blueRocket2.ycor()
    by2 += 2
    blueRocket2.sety(by2)

    bx2 = blueRocket2.xcor()
    bx2 += 4
    blueRocket2.setx(bx2)


    by3 = blueRocket3.ycor()
    by3 += 2
    blueRocket3.sety(by3)

    bx3 = blueRocket3.xcor()
    bx3 -= 4
    blueRocket3.setx(bx3)


    by4 = blueRocket4.ycor()
    by4 += 2
    blueRocket4.sety(by4)

    bx4 = blueRocket4.xcor()
    bx4 += 3
    blueRocket4.setx(bx4)

while True:
    wn.update()
