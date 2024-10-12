import time
from turtle import Turtle, Screen
import constants



class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        
    def create_snake(self):
        for position in constants.STARTING_POSITIONS:
            self.add_segment(position)
    '''
    https://www.udemy.com/course/100-days-of-code/learn/lecture/20356939#overview
    Minute: 11 explaination of the snake movement in this function.
    '''
    def move(self):
        for snake_num in range(len(self.snakes)-1, 0, -1):
            cord_x= self.snakes[snake_num-1].xcor()
            cord_y= self.snakes[snake_num-1].ycor()
            self.snakes[snake_num].goto(cord_x, cord_y)
        self.head.forward(constants.MOVE_DISTANCE)
    
    def extend_snake(self):
        self.add_segment(self.snakes[-1].position())
    def add_segment(self, position):
        snake = Turtle(shape=constants.SNAKE_SHAPE)
        snake.color(constants.SNAKE_COLOR)
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)
        
    #? right arrow = 0º
    #? left arrow = 180º
    #? up arrow = 90º
    #? down arrow = 270º
    def up(self):
        if self.head.heading()!= constants.DOWN:
            self.head.setheading(constants.UP)
    def down(self):
        if self.head.heading()!= constants.UP:
            self.head.setheading(constants.DOWN)
    def left(self):
        if self.head.heading()!= constants.RIGHT:
            self.head.setheading(constants.LEFT)
    def right(self):
        if self.head.heading()!= constants.LEFT:
            self.head.setheading(constants.RIGHT)