import turtle as t
import random
tim = t.Turtle()
num_sides = 3
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Create a turtle object
tim.shape("turtle")
tim.penup()
# Set the initial position to (100, 100)
tim.goto(20, 100)

# Set the line size to 5 pixels
tim.width(5)

# Set the drawing speed to 3 (medium speed)
tim.speed(3)
tim.pendown()
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle= 360/num_sides
        tim.forward(100)
        tim.right(angle)
screen = t.Screen()

# Set the dimensions of the turtle window
screen.setup(width=800, height=600)
#for shape_side in range(3,11):
#    draw_shape(shape_side)
#    
for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen.exitonclick()