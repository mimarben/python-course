import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import constants

screen = Screen()
screen.title(constants.APP_TITLE)
screen.setup(height=constants.SCREEN_HEIGHT, width= constants.SCREEN_WIDTH)
screen.bgcolor(constants.SCREEN_BGCOLOR)
screen.tracer(0)
snake= Snake()
food = Food()
socoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(constants.TIME_REFRESH)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.extend_snake()
        socoreboard.increase_scoreboard()
        
    # Detect collision with walls    
    if snake.head.xcor() > constants.SCREEN_LIMIT_WIDTH or snake.head.xcor() < -constants.SCREEN_LIMIT_WIDTH or snake.head.ycor() > constants.SCREEN_LIMIT_HEIGHT or snake.head.ycor()< -constants.SCREEN_LIMIT_HEIGHT:
        game_is_on = False
        socoreboard.game_over()
    
    # Detect collision with snake tail
    for segment in snake.snakes[1:]:
        #if segment == snake.head:
        #    pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            socoreboard.game_over()


screen.exitonclick()
