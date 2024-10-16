from turtle import Turtle

STARTING_POSITION = (0, -280)
STARTING_MOVE_DISTANCE = 5
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.speed('fastest') 
        self.setheading(90)

    def go_up(self):
        self.forward(STARTING_MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Detect sussesfull crossing of the finish line.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False