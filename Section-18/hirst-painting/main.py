###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
import random as rd

tim = t.Turtle()
rgb_colors = []
t.colormode(255)
tim.speed("fastest")
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b= color.rgb.b
    rgb_colors.append((r, g, b))


tim.shape("circle")
tim.penup()
number_of_dots = 100
tim.hideturtle()
for dot_count in range(1,number_of_dots):
    tim.dot(20, rd.choice(rgb_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


# Set the line size to 5 pixels
tim.width(10)

# Set the drawing speed to 3 (medium speed)
tim.speed(1)
tim.pendown()

screen = t.Screen()
# Set the dimensions of the turtle window
screen.setup(width=800, height=600) 

screen.exitonclick()