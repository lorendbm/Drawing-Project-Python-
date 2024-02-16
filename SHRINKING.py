import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("red")
drawing_board.title("DRAWING WINDOW")
cursor_instance = turtle.Turtle()
cursor_instance.color("white")
cursor_instance.width(5)


def shrinking_square(size):
    for i in range(20):
        cursor_instance.forward(size)
        cursor_instance.left(90)
        size = size - 10

shrinking_square(200)
#shrinking_square(150)
#shrinking_square(100)
#shrinking_square(50)
turtle.done()


