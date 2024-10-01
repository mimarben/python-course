import turtle as t
import random
tim = t.Turtle()
num_sides = 3
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angle = [90, -90]
direction=["left", "right"]
# Create a turtle object
tim.shape("arrow")
tim.penup()
# Set the initial position to (100, 100)
tim.goto(20, 100)

# Set the line size to 5 pixels
tim.width(10)

# Set the drawing speed to 3 (medium speed)
tim.speed(1)
tim.pendown()

screen = t.Screen()
# Set the dimensions of the turtle window
screen.setup(width=800, height=600) 
t.colormode(255)
def draw_shape(distance, direction, angle):
    if direction == "left":
        tim.left(angle)
    elif direction == "right":
        tim.right(angle)
    tim.color(random_color())
    tim.forward(distance)

def random_color():
    r= random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return (r, g, b)
      
while True:
    draw_shape(random.randint(50, 100), random.choice(direction), random.choice(angle))
    print (random.randint(50, 100))

screen = t.Screen()
screen.exitonclick()
