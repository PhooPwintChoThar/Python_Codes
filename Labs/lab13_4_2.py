import turtle


def draw_pic():
    for i in range(4):
        turtle.left(90)
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.right(90)
        turtle.backward(120.5)
        turtle.left(90)
        turtle.forward(120.5)


draw_pic()
turtle.done()