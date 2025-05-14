import turtle
import random

# --- Screen Setup ---
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# --- Paddle ---
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# --- Ball ---
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 2
ball.dy = 2

# --- Bricks ---
bricks = []

colors = ["red", "orange", "yellow", "green", "blue"]

for row in range(5):
    for col in range(-350, 400, 70):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(col, 250 - row * 30)
        bricks.append(brick)

# --- Movement ---
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 40)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 40)

win.listen()
win.onkeypress(paddle_left, "Left")
win.onkeypress(paddle_right, "Right")

# --- Game Loop ---
running = True
while running:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collision
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() < -230 and ball.ycor() > -240) and \
       (paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60):
        ball.sety(-230)
        ball.dy *= -1

    # Bottom collision (Game Over)
    if ball.ycor() < -290:
        ball.goto(0, -200)
        ball.dx = 2
        ball.dy = 2
        print("Game Over")
        running = False

    # Brick collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move it off-screen
            bricks.remove(brick)
            break

    # Win condition
    if not bricks:
        print("You Win!")
        running = False
