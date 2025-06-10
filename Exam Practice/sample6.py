import turtle
import math

def draw_square(n):
    for i in range(4):
        turtle.forward(n)
        turtle.right(90)

def draw_nested_squares(s,g):
    turtle.penup()
    while s>=20:
        half=s/2
        turtle.left(90)
        turtle.forward(half)
        turtle.left(90)
        turtle.forward(half)
        turtle.right(180)
        turtle.pendown()
        draw_square(s)
        turtle.penup()
        s=s-(g*2)
        turtle.goto(0,0)


draw_nested_squares(200,20)
turtle.done()
        