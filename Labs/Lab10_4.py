import turtle 

def draw(list):
    new=[]
    for x in list:
        if x in new:
            continue
        else:
            new.append(x)

    new.sort()

    highestcount=0

    for a in new:
        count=0
        for b in list:
            if b==a:
                count+=1
            else:
                continue
        if count>highestcount:
            highestcount=count

    turtle.forward(30*(len(new)+1))
    turtle.home()
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20*highestcount)
    turtle.home()
    turtle.penup()
    turtle.forward(30)
    turtle.begin_fill()
    turtle.color("purple")

    for a in new:
        turtle.goto(turtle.xcor(),turtle.ycor()-15)
        turtle.write(a)
        turtle.goto(turtle.xcor(),turtle.ycor()+15)
        turtle.left(90)
        turtle.pendown()
        distance=0
        for b in list:
            if b==a:
                turtle.forward(20)
                distance+=1
            else:
                continue
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(distance*20)
        turtle.left(90)
        turtle.penup()
    turtle.end_fill()
    turtle.home()
    turtle.right(90)
    turtle.forward(50)
    turtle.done()



list1=[1,2,2,1,3,4,6,5,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4]
draw(list1)

