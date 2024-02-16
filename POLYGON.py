import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("gray")
drawing_board.title("DRAWING WINDOW")
cursor_instance = turtle.Turtle()
cursor_instance.width(5)
cursor_instance.color("red")

#REGULAR POLYGON (INPUT)
number_of_sides = input("How many sides you want ?: ")
angle = 360.0 / int(number_of_sides)
side_lenght = input("enter lenght: ")

for b in range(int(number_of_sides)):
    cursor_instance.right(angle)
    cursor_instance.forward(int(side_lenght))
turtle.done()
