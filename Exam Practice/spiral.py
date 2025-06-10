import turtle

def draw_sq(n):
    for i in range(4):
        turtle.forward(n)
        turtle.right(90)

def spiral_sq(s):
    degree=90
    while s>=5:
        turtle.penup()
        turtle.left(degree)
        turtle.forward(s/2)
        turtle.right(90)
        turtle.backward(s/2)
        turtle.pendown()
        draw_sq(s)
        turtle.penup()
        turtle.goto(0,0)
        turtle.setheading(0)
        degree+=10
        s*=0.75


spiral_sq(150)
turtle.goto(0,0)
turtle.right(225)
turtle.done()