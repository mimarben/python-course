from turtle import Turtle
import constants

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape(constants.PADDLE_SHAPE)
        self.color(constants.PADDLE_COLOR)
        self.shapesize(stretch_wid=constants.PADDLE_WID, stretch_len=constants.PADDLE_LEN)
        self.penup()
        self.goto(position)
        

    def go_up(self):
        new_y = self.ycor()+20
        if new_y < constants.SCREEN_LIMIT_HEIGHT:
            self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor()-20
        if new_y > -constants.SCREEN_LIMIT_HEIGHT:
            self.goto(self.xcor(), new_y)
