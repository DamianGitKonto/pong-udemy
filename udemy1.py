

import turtle

wn = turtle.Screen()
wn.title("Pong by Damian")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.penup()
paddle_a.goto(0, 270)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=1, stretch_len=5)
paddle_b.penup()
paddle_b.goto(0, -270)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.1

# Function
def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)


def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)


def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)


def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")
wn.onkeypress(paddle_b_right, "Right")
wn.onkeypress(paddle_b_left, "Left")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.goto(0, 0)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() > -280 and ball.xcor() < -290) and (ball.xcor() < paddle_b.xcor() + 40 and ball.xcor() > paddle_b.xcor() -40):
        ball.sety(270)
        ball.dy *= -1