import turtle
import random

def DrawPieChart(list):
    uniqueNumbers=[]
    for x in list:
        if x in uniqueNumbers:
            continue
        else:
            uniqueNumbers.append(x)
    colorNames = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 
                   'brown', 'gray', 'cyan', 'magenta', 'lime', 
                   'teal', 'indigo', 'violet', 'gold', 'silver', 'maroon']
    colors=[]
    for y in range(len(uniqueNumbers)):
        color=random.choice(colorNames)
        while color in colors:
            color=random.choice(colorNames)
        colors.append(color)
    
    degreePerNumber=360/len(list)
    radius=100
    turtle.penup()
    turtle.goto(0,-radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.home()
    turtle.pendown()
    startangle=0
    for each in range(len(uniqueNumbers)):
        totalDegree=0
        for all in list:
            if all==uniqueNumbers[each]:
                totalDegree+=degreePerNumber
            else:
                continue
        startangle+=totalDegree
        turtle.begin_fill()
        turtle.fillcolor(colors[each])
        turtle.forward(radius)
        turtle.left(90)
        turtle.circle(radius, totalDegree)
        turtle.home()
        turtle.setheading(startangle)
        turtle.end_fill()
    

    turtle.penup()
    turtle.goto(0,-radius-50)
    for t in range(len(uniqueNumbers)):
        turtle.write(f"{uniqueNumbers[t]}={colors[t]}\n")
        turtle.goto(turtle.xcor(),turtle.ycor()-15)
    turtle.done()



list1=[3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3]
DrawPieChart(list1)