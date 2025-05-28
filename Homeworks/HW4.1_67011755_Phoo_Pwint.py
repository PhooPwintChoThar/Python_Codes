import turtle
print("x and y coordinates for point 0")
x0=int(input("x : "))
y0=int(input("y : "))

print("x and y coordinates for point 1")
x1=int(input("x : "))
y1=int(input("y : "))

print("x and y coordinates for point 2")
x2=int(input("x : "))
y2=int(input("y : "))

slope_of_line=(y1-y0)/(x1-x0)

slope_of_line2=(y2-y0)/(x2-x0)

if slope_of_line==slope_of_line2:
    message="p2 is on the line"
elif slope_of_line2>slope_of_line:
    message="p2 is on the left side of the line between p0 and p1."
else:
    message="p2 is on the right side of the line between p0 and p1."



turtle.penup()
turtle.goto(x0,y0+5)
turtle.write(f"P0({x0} , {y0})")
turtle.goto(x0,y0)
turtle.pendown()
turtle.goto(x1,y1)
turtle.penup()
turtle.goto(x1,y1+5)
turtle.write(f"P1({x1} , {y1})")
turtle.penup()
turtle.goto(x2,y2)
turtle.write(f"P2({x2} , {y2})")
turtle.goto(x2,y2-15)
turtle.write(message)
turtle.goto(x2,y2)
turtle.done()





