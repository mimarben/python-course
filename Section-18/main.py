from turtle import Turtle, Screen

figure = Turtle()
figure.shape('arrow')
figure.color('blue')





screen = Screen()
# Set the dimensions of the turtle window
screen.setup(width=800, height=600)

for _ in range(4):
    figure.forward(100)
    figure.right(90)
    
 
########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    figure.forward(10)
    figure.penup()
    figure.forward(10)
    figure.pendown()
        
screen.exitonclick()