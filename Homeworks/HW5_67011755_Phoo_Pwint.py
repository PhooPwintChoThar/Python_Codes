#No.1
n=int(input("Type a number which you want to find it square root : "))
guess=n/2
temp=n/guess
guess=(guess+temp)/2

for x in range(5):
    temp=n/guess
    guess=(guess+temp)/2
print("Square root of",n," by iterating 5 times: ",format(guess,".3f"))
for y in range(6):
    temp=n/guess
    guess=(guess+temp)/2
print("Square root of",n," by iterating 6 times: ",format(guess,".3f"))
for z in range(7):
    temp=n/guess
    guess=(guess+temp)/2
print("Square root of",n," by iterating 7 times: ",format(guess,".3f"))

#No.2
import turtle
start_x=-630
start_y=330
start_count=1

turtle.speed(0)
turtle.penup()
for month in range(1,13):
    if month ==4 or month==6 or month==9 or month==11:
        days=30
    elif month==2:
        days=29
    else:
        days=31 
    sq_count=0   
    day=1
    turtle.goto(start_x,start_y)
    turtle.pendown()
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(140)
    turtle.write("  Month#"+str(month))
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.penup()
    turtle.goto(start_x,turtle.ycor()-40)
    count=0
    for c in range(7):
        count+=1
        turtle.pendown()
        for square in range(4):
            turtle.forward(20)
            turtle.left(90)
        if count==1:
            turtle.write(" Su")
        elif count==2:
            turtle.write("  Mo")
        elif count==3:
            turtle.write("  Tu")
        elif count==4:
            turtle.write(" We")
        elif count==5:
            turtle.write("  Th")
        elif count==6:
            turtle.write("  Fr")
        else:
            turtle.write("  Sa")   
        turtle.forward(20)
    turtle.penup()

    d_start_y=start_y-60
    d_start_x=start_x
    d_start=(start_x,d_start_y)
    turtle.goto(d_start)
    for row in range(6):
        for col in range(7):
            turtle.pendown()
            if sq_count==start_count:
                    if day==days+1:
                       start_count=sq_count%7
                    elif day>days+1:
                        start_count-=1
                    else:
                        turtle.write("  "+str(day))
                        start_count+=1
                        day+=1
            for square in range(4):
                turtle.forward(20)
                turtle.left(90)
                
                    
            turtle.penup()
            turtle.forward(20)
            sq_count+=1
        turtle.penup()
        turtle.goto(d_start_x,turtle.ycor()-20)

    if month%3==0:
        start_x=start_x+200
        start_y=start_y+400
    else:
        start_y=start_y-200
turtle.done()


#No.3
integer=int(input("Enter any integer greater than or equal to 1 : "))
while integer<1:
    integer=int(input("Invalid!\nEnter any integer greater than or equal to 1 : "))
if integer==1:
    print("*")
else:
    for a in range(integer,-1,-1):
        if a==0:
            print("*")
            break
        for b in range (a):
            for c in range (b+1):
                print("*",end="")
            print("\n")
            if b==a-1:
                for d in range(b-1):
                    for e in range (b-d):
                        print("*",end="")
                    print("\n")

    

    
