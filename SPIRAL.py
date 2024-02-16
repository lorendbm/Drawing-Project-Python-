import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("cyan")
drawing_board.title("DRAWING WINDOW")
cursor_instance = turtle.Turtle()
cursor_instance.width(10)

cursorColors = ["Magenta","Red","Yellow","White","Black","Orange"]

for i in range(20):
    cursor_instance.color(cursorColors[i % 6])
    cursor_instance.circle(15 * i)
    cursor_instance.circle(-15 * i)
turtle.done()