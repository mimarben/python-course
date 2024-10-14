import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

import constants
screen = Screen()
screen.title(constants.APP_TITLE)
screen.setup(height=constants.SCREEN_HEIGHT, width= constants.SCREEN_WIDTH)
screen.bgcolor(constants.SCREEN_BGCOLOR)
screen.tracer(0)


r_paddle = Paddle((constants.SCREEN_LIMIT_WIDTH,0))
l_paddle = Paddle((-constants.SCREEN_LIMIT_WIDTH,0))
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(constants.GAME_SPEED)


screen.exitonclick()