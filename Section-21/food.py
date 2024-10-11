from turtle import Turtle
import random
import constants

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(constants.FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(constants.FOOD_COLOR)
        self.speed(constants.FOOD_SPEED)
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randint(-int((constants.SCREEN_WIDTH/2)-constants.SCREEN_GAP), int((constants.SCREEN_HEIGHT/2)-constants.SCREEN_GAP))
        random_y = random.randint(-int((constants.SCREEN_HEIGHT/2)-constants.SCREEN_GAP), int((constants.SCREEN_HEIGHT/2)-constants.SCREEN_GAP))
        self.goto(random_x, random_y)