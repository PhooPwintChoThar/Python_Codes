import turtle
def draw_arrow():
    turtle.begin_fill()
    turtle.color("black")
    turtle.left(120)
    turtle.forward(7)
    turtle.right(160)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.penup()


text=input("Enter some text : ")
check=''
for c in text:
    if c in check:
        continue
    else:
        check+=c

highestCount=0

for a in check:
    count=0
    for b in text:
        if b==a:
            count+=1
        else:
            continue
    if count>highestCount:
        highestCount=count

turtle.forward(30*(len(check)+1))
draw_arrow()
turtle.home()
turtle.left(90)
turtle.pendown()
turtle.forward(20*highestCount)
draw_arrow()
turtle.home()

for a in check:
    turtle.forward(20)
    turtle.goto(turtle.xcor(),turtle.ycor()-15)
    turtle.write(a)
    turtle.goto(turtle.xcor(),turtle.ycor()+15)
    turtle.left(90)
    turtle.pendown()
    distance=0
    for b in text:
        if b==a:
            turtle.forward(20)
            distance+=1
        else:
            continue
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(distance*20)
    turtle.left(90)
    turtle.penup()

turtle.home()
turtle.right(90)
turtle.forward(50)
turtle.done()
