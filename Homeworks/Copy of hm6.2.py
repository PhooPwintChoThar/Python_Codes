import turtle
def calenderMonth(month):
    daysBeforeMonth=0
    daysInMonth=0
    for i in range(1,month+1):
        if i==2:
            days=29
        elif i==4 or i==6 or i==9 or i==11:
            days=30
        else:
            days=31
        if i==month:
            daysInMonth=days
        else:
            daysBeforeMonth+=days

    if month==1:
        monthName="January"
    elif month==2:
        monthName="February"
    elif month==3:
        monthName="March"
    elif month==4:
        monthName="April"
    elif month==5:
        monthName="May"
    elif month==6:
        monthName="June"
    elif month==7:
        monthName="July"
    elif month==8:
        monthName="August"
    elif month==9:
        monthName="September"
    elif month==10:
        monthName="October"
    elif month==11:
        monthName="November"
    elif month==12:
        monthName="December"
    
    turtle.speed(0)
    turtle.forward(210)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(105)
    turtle.write(monthName+"2024", align="center")
    turtle.forward(105)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.penup()
    dayText=0
    y=-30
    turtle.goto(0,y)
    for square in range(1,50):
        if square<=7:
            if square==1:
                text="Mon"
            elif square==2:
                text="Tue"
            elif square==3:
                text="Wed"
            elif square==4:
                text="Thu"
            elif square==5:
                text="Fri"
            elif square==6:
                text="Sat"
            else:
                text="Sun"
        elif square<=((daysBeforeMonth%7)+7):
            text=""
        else:
            if dayText>=daysInMonth:
                text=""
            else:
                dayText+=1
                text=str(dayText)
        turtle.pendown()
        for i in range(1,5):
            if i==3:
                turtle.forward(15)
                turtle.write(text,align="center")
                turtle.forward(15)
            else:
                turtle.forward(30)
            turtle.right(90)
        turtle.penup()
        if square%7==0:
            y-=30
            turtle.goto(0,y)
        else:
            turtle.forward(30)
    turtle.done()
calenderMonth(12)

        