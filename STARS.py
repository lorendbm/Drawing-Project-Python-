import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("purple")
drawing_board.title("DRAWING WINDOW")
cursor_instance = turtle.Turtle()
cursor_instance.color("yellow")
cursor_instance.width(10)

#STAR (MARSHALL)
y = 0
while y < 6:
    cursor_instance.forward(150)
    cursor_instance.left(60)
    cursor_instance.forward(150)
    cursor_instance.right(120)
    y += 1
turtle.done()

#STAR (NORMAL)
#z = 0
#while z < 5:
    #cursor_instance.forward(150)
    #cursor_instance.left(60)
    #cursor_instance.forward(150)
    #cursor_instance.right(132)
    #z += 1
#turtle.done()

#STAR (HANDMADE)
#a = 0
#while a < 9:
    #cursor_instance.forward(200)
    #cursor_instance.right(160)
    #a += 1
#turtle.done()