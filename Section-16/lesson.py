from turtle import Turtle, Screen
import import_module
import prettytable as pt

print(import_module.varaible)

#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("blue")
#timmy.forward(50)
#my_screen = Screen();
#print(my_screen.canvheight)
#my_screen.exitonclick()

table = pt.PrettyTable(["Name", "Type", "Value"])
table.add_row(["Variable", "Global", import_module.varaible])
table.align="l"
print(table)