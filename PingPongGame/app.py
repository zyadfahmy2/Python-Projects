import turtle
# the file turtle containes a class Screen which shows the screen when created
wind = turtle.Screen()
wind.title("Ping Pong By Ziad")
wind.bgcolor("black")
wind.setup(width=800, height=600)
#now we need to prevent the screen from updating itself automatically we want to do it manually
# wind.tracer(0)

#rectangle 1
rect1 = turtle.Turtle()
rect1.color("blue")
#making the turlte object speed fast where the top speed is 0
rect1.speed(0)
rect1.shape("square")
rect1.shapesize(5, 1)
rect1.penup()
rect1.goto(-350, 0)

#rectangle 2
rect2 = turtle.Turtle()
rect2.color("red")
#making the turlte object speed fast where the top speed is 0
rect2.speed(0)
rect2.shape("square")
rect2.shapesize(5, 1)
rect2.penup()
rect2.goto(350, 0)

#ball
circle = turtle.Turtle()
circle.color("white")
#making the turlte object speed fast where the top speed is 0
circle.speed(0)
circle.shape("square")
circle.penup()
#making the change in x (delta x ) = 2.5
circle.dx = 4.5
circle.dy = 4.5
# circle.goto(0,0)
score1 = 0
score2 = 0
score = turtle.Turtle()
score.penup()
score.color("white")
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 | player 2: 0", align="center", font=("Courier", 20, "normal"))
def rect1_up():
    y = rect1.ycor() #get the coordinates of y
    if y <= 250:
        y +=20
    rect1.sety(y)
def rect1_down():
    y = rect1.ycor()
    if y>-240:
        y -=20
    rect1.sety(y)

#function for rect2

def rect2_up():
    y = rect2.ycor()
    if y < 250:
        y +=20
    rect2.sety(y)
def rect2_down():
    y = rect2.ycor()
    if y>-240:
        y -=20
    rect2.sety(y)

#listen for anyy input
wind.listen()
wind.onkeypress(rect1_up, "w")
wind.onkeypress(rect1_down, "s")
wind.onkeypress(rect2_up, "Up")
wind.onkeypress(rect2_down, "Down")

#we will make a loop that updates the screen so it won't be turned off
while True:
    wind.update()
    circle.setx(circle.xcor()+circle.dx) # ball starts at zero and everytime loop runs it moves 4.5 on x axis
    circle.sety(circle.ycor() + circle.dy)
    # if the circle reaches the top or bottom reverse its direction
    if circle.ycor() > 290:
        circle.sety(290)
        circle.dy*=-1;
    if circle.ycor() < -290:
        circle.sety(-290)
        circle.dy*=-1;

    #if the rects didn't catch the ball the ball is returned to center and direnction is reversed

    if circle.xcor() >390:
        circle.setx(0)
        circle.sety(0)
        circle.dx *= -1;
        score1+= 1
        score.clear()
        score.write("player 1: {} | player 2: {}".format(score1,score2), align="center", font=("Courier", 20,"normal"))
    if circle.xcor() <-390:
        circle.goto(0,0)
        circle.dx *= -1;
        score2 += 1
        score.clear()
        score.write("player 1: {} | player 2: {}".format(score1, score2), align="center", font=("Courier", 20,"normal"))

    if circle.xcor() >340 and circle.xcor() <350 and  circle.ycor() <= rect2.ycor()+50 and circle.ycor() >= rect2.ycor()-50:
        circle.setx(340)
        circle.dx *= -1

    if circle.xcor() <-340 and circle.xcor() > -350 and  circle.ycor() <= rect1.ycor()+50 and circle.ycor() >= rect1.ycor()-50:
        circle.setx(-340)
        circle.dx *= -1
