from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=800, height=800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color:")




screen.exitonclick()