import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("DRAW!!!")
cursor_instance = turtle.Turtle()

def cursor_forward():
    cursor_instance.forward(50)
def rotate_angle_right():
    cursor_instance.right(10)
def rotate_angle_left():
    cursor_instance.left(10)
def clear_screen():
    cursor_instance.clear()

def cursor_pen_up():
    cursor_instance.penup()

def cursor_pen_down():
    cursor_instance.pendown()
def cursor_return_home():
    cursor_instance.penup()
    cursor_instance.home()
    cursor_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=cursor_forward, key="space")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=cursor_return_home, key="h")

drawing_board.exitonclick()
turtle.done()

