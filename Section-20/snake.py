import time
from turtle import Turtle, Screen

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)
    def move(self):
        for snake_num in range(len(self.snakes)-1, 0, -1):
            cord_x= self.snakes[snake_num-1].xcor()
            cord_y= self.snakes[snake_num-1].ycor()
            self.snakes[snake_num].goto(cord_x, cord_y)
        self.head.forward(MOVE_DISTANCE)
    
    #? right arrow = 0º
    #? left arrow = 180º
    #? up arrow = 90º
    #? down arrow = 270º
    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)