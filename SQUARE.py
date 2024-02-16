import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("cyan")
drawing_board.title("DRAWING WINDOW")
cursor_instance = turtle.Turtle()
cursor_instance.width(20)
cursor_instance.color("brown")

#SQUARE
x = 0
while x < 4:
    cursor_instance.forward(300)
    cursor_instance.left(90)
    x += 1
turtle.done()