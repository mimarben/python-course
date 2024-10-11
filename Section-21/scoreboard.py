from turtle import Turtle
import constants

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, (constants.SCREEN_LIMIT_WIDTH-10))
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=constants.SCORE_ALIGNMENT, font=constants.SCORE_FONT)
    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=constants.SCORE_ALIGNMENT, font=constants.SCORE_FONT)