# Simple Pong in Python 3 for Beginners
# By Gabriel Yturaldi
# Part 1: Getting Started

# Import packages

# Turtle is used for graphics
import turtle

# Pygame is used for the timeout when the game is over
import pygame

# Create Screen
wn = turtle.Screen()
wn.title("Pong by Gabriel Yturaldi")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# Create Turtle objects

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = .1
ball.dy = -.1

# Pen
pen = turtle.Turtle()
pen.speed()
pen.color("white")
#pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Red: 0 Blue: 0", align="center", font=("Courier", 24, "normal"))

# Create Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop

game_over = False

while not game_over:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for the ball
    if ball.ycor() > 300:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -300:
        ball.sety(-290)
        ball.dy *= -1


    # Border checking for the paddles
    if paddle_a.ycor() > 240:
        paddle_a.sety(240)

    if paddle_a.ycor() < -240:
        paddle_a.sety(-240)

    if paddle_b.ycor() > 240:
        paddle_b.sety(240)

    if paddle_b.ycor() < -240:
        paddle_b.sety(-240)


    # Check to see if ball went off screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Red: {} Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx = -.1
        ball.color("white")


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Red: {} Blue: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx = .1
        ball.color("white")

    # Paddle and ball collisions

    # Paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() <  paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1.3
        ball.color("blue")

    # Paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <  paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1.3
        ball.color("red")

    # Check scores
    if score_a == 10:
        pen.clear()
        pen.color("red")
        pen.write("Red wins!!", align="center", font=("Courier", 24, "normal"))
        pygame.time.wait(3000)
        game_over = True
    elif score_b == 10:
        pen.clear()
        pen.color("blue")
        pen.write("Blue wins!!", align="center", font=("Courier", 24, "normal"))
        pygame.time.wait(3000)
        game_over = True