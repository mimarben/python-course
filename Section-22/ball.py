from turtle import Turtle
import constants
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(constants.BALL_SHAPE)
        self.color(constants.BALL_COLOR)
        self.penup()
        self.goto(0, 0)
        self.dx = constants.BALL_X_POS
        self.dy = constants.BALL_Y_POS
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy        
        self.goto(new_x, new_y)
    def bounce_y(self):
         self.dy *= -1
    def bounce_x(self):
         self.dx *= -1
         self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1       
        self.bounce_x()