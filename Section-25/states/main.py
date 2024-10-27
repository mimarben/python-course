import turtle as turtle
import pandas as pnd
import random as rnd

screen = turtle.Screen()
screen.title("U.S. States Game")
turtle.shape("circle")
image = "./blank_states_img.gif"
screen.register_shape(image)
turtle.shape(image)
screen.tracer(0)
screen.setup(width=725, height=491)
screen.update()

#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#screen.onscreenclick(get_mouse_click_coor)

data = pnd.read_csv("50_states.csv")
all_states= data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pnd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t =turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state==answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item(), align="center", font=("Arial", 10, "normal"))    

#turtle.mainloop()
#turtle.exitonclick()

