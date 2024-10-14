import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import constants
screen = Screen()
screen.title(constants.APP_TITLE)
screen.setup(height=constants.SCREEN_HEIGHT, width= constants.SCREEN_WIDTH)
screen.bgcolor(constants.SCREEN_BGCOLOR)
screen.tracer(0)


r_paddle = Paddle((constants.PADDLE_POSSTION,0))
l_paddle = Paddle((-constants.PADDLE_POSSTION,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

print(f'PADDLE_POSSTION RIGHT: {constants.PADDLE_POSSTION}')
print(f'PADDLE_POSSTION left: {-constants.PADDLE_POSSTION}')
print(f'LIMIT WIDTH: {constants.SCREEN_LIMIT_WIDTH}')
print(f'lIMIT HEIGHT: {constants.SCREEN_LIMIT_HEIGHT}')
print(f'PADDLE MISSED: {constants.PADDLE_MISSED}')
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > constants.SCREEN_LIMIT_HEIGHT or ball.ycor() < -constants.SCREEN_LIMIT_HEIGHT:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > constants.SCREEN_LIMIT_WIDTH or ball.distance(l_paddle) < 50 and ball.xcor() < -constants.SCREEN_LIMIT_WIDTH:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > constants.PADDLE_MISSED:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -constants.PADDLE_MISSED:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()