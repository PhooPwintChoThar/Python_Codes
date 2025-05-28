import turtle
print("For  green rectangle")
x_of_green=eval(input("x coordinate of center : "))
y_of_green=eval(input("y coordinate of center : "))
width_of_green=eval(input("width : "))
height_of_green=eval(input("height : "))

print("\n")

print("For  blue rectangle")
x_of_blue=eval(input("x coordinate of center : "))
y_of_blue=eval(input("y coordinate of center : "))
width_of_blue=eval(input("width : "))
height_of_blue=eval(input("height : "))


x1_g=x_of_green - width_of_green
y1_g=y_of_green + height_of_green
x2_g=x_of_green + width_of_green
y2_g=y_of_green + height_of_green
x3_g=x_of_green + width_of_green
y3_g=y_of_green - height_of_green
x4_g=x_of_green - width_of_green
y4_g=y_of_green - height_of_green
point1_green=( x1_g , y1_g )
point2_green=( x2_g , y2_g )
point3_green=( x3_g , y3_g )
point4_green=( x4_g , y4_g)

x1_b=x_of_blue - width_of_blue
y1_b=y_of_blue + height_of_blue
x2_b=x_of_blue + width_of_blue
y2_b=y_of_blue + height_of_blue
x3_b=x_of_blue + width_of_blue
y3_b=y_of_blue - height_of_blue
x4_b=x_of_blue - width_of_blue
y4_b=y_of_blue - height_of_blue
point1_blue=( x1_b , y1_b )
point2_blue=( x2_b , y2_b )
point3_blue=( x3_b , y3_b )
point4_blue=( x4_b , y4_b )


if(x1_g==x1_b and y1_b==y1_g) and (x2_g==x2_b and y2_b==y2_g) and\
   (x3_g==x3_b and y3_b==y3_g) and (x4_g==x4_b and y4_b==y4_g):
    message="The blue rectangle and the green rectangle are identical."
elif((x1_g<=x1_b and x1_b<=x2_g) and (y4_g<=y1_b and y1_b<=y1_g)) and\
    ((x1_g<=x2_b and x2_b<=x2_g) and (y4_g<=y2_b and y2_b<=y1_g)) and\
    ((x1_g<=x3_b and x3_b<=x2_g) and (y4_g<=y3_b and y3_b<=y1_g)) and\
    ((x1_g<=x4_b and x4_b<=x2_g) and (y4_g<=y4_b and y4_b<=y1_g)):
    message="The blue rectangle is inside the green rectangle."
elif((x1_b<=x1_g and x1_g<=x2_b) and (y4_b<=y1_g and y1_g<=y1_b)) and\
    ((x1_b<=x2_g and x2_g<=x2_b) and (y4_b<=y2_g and y2_g<=y1_b)) and\
    ((x1_b<=x3_g and x3_g<=x2_b) and (y4_b<=y3_g and y3_g<=y1_b)) and\
    ((x1_b<=x4_g and x4_g<=x2_b) and (y4_b<=y4_g and y4_g<=y1_b)):
    message="The green rectangle is inside the blue rectangle."
elif((x1_b<=x1_g and x1_g<=x2_b) and (y4_b<=y1_g and y1_g<=y1_b)) or\
    ((x1_b<=x2_g and x2_g<=x2_b) and (y4_b<=y2_g and y2_g<=y1_b)) or\
    ((x1_b<=x3_g and x3_g<=x2_b) and (y4_b<=y3_g and y3_g<=y1_b)) or\
    ((x1_b<=x4_g and x4_g<=x2_b) and (y4_b<=y4_g and y4_g<=y1_b)):
    message="The blue rectangle and the green rectangle are overlap."
else:
    message="The blue rectangle and the green rectangle are outside each other."
     

turtle.penup()
turtle.color("green")
turtle.goto( x_of_green , y_of_green )
turtle.write(f"({x_of_green},{y_of_green})")
turtle.goto(point1_green)
turtle.pendown()
turtle.goto(point2_green)
turtle.right(90)
turtle.goto(point3_green)
turtle.right(90)
turtle.goto(point4_green)
turtle.right(90)
turtle.goto(point1_green)
turtle.penup()

turtle.color("blue")
turtle.goto( x_of_blue , y_of_blue )
turtle.write(f"({x_of_blue},{y_of_blue})")
turtle.goto(point1_blue)
turtle.pendown()
turtle.goto(point2_blue)
turtle.right(90)
turtle.goto(point3_blue)
turtle.right(90)
turtle.goto(point4_blue)
turtle.right(90)
turtle.goto(point1_blue)
turtle.penup()
turtle.goto(point4_blue)
turtle.sety(y4_b-15)
turtle.color("red")
turtle.write(message)
turtle.done()
