from turtle import Turtle
import constants

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(constants.BALL_SHAPE)
        self.color(constants.BALL_COLOR)
        self.penup()
        self.goto(0, 0)
        self.dx = constants.BALL_X_POS
        self.dy = constants.BALL_Y_POS
        
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        
        if (new_x < -constants.SCREEN_LIMIT_WIDTH or new_x > constants.SCREEN_LIMIT_WIDTH):
            print(f"Before x: {self.dx}")
            self.dx *= -1
            print(f"After x: {self.dx}")
        if (new_y < -constants.SCREEN_LIMIT_HEIGHT or new_y > constants.SCREEN_LIMIT_HEIGHT):
            print(f"Before y: {self.dy}")
            self.dy *= -1
            print(f"After y: {self.dy}")
        self.goto(new_x, new_y)