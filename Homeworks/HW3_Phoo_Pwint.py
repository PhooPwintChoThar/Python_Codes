print("\n#No.1\n")
name=input("Enter employee's Name : ")
hours_worked=float(input("Enter number of hours worked in a week : "))
pay_rate=float(input("Enter hourly pay rate : "))
federal_tax_rate=float(input("Enter federal tax withholding rate : "))
state_tax_rate=float(input("Enter state tax withholding rate : "))

print("\n")
print("Employee Name : ",name)
print("Hours Worked : ", hours_worked)
print("Pay Rate : $"+str(pay_rate))

gross_pay=hours_worked * pay_rate
print("Gross Pay : $" +str(round(gross_pay,2)))

federal_tax=gross_pay * federal_tax_rate
state_tax=gross_pay * state_tax_rate
total_deduction=federal_tax + state_tax
print("Deductions:")
print(f"\tFederal Withholding({format(federal_tax_rate, "5.2%")}) : $" + str(round(federal_tax,2)))
print(f"\tState Withholding ({format(state_tax_rate, "5.2%")}) : $" + str(round(state_tax,2)))
print(f"\tTotal Deduction : $" + str(round(total_deduction,2)))

net_pay=gross_pay - total_deduction
print("Net Pay : $" + str(round(net_pay,2)))


print("\n#No.2\n")
typed_number=input("Enter a four-digit integer:")
while len(typed_number) >4:
    print("Please type only 4 digits. ")
    typed_number=input("Enter a four-digit integer:")
else :
    print("The number you typed is :  ", typed_number)
    reversed_number=""
    x=len(typed_number)-1
    while x>=0:
      reversed_number+=typed_number[x]
      x-=1
    print("The number in reverse order is : ", reversed_number)



print("\n#No.3\n")
import turtle
length=int(input("Enter the length of the star : "))
turtle.left(72)
turtle.forward(length)
turtle.right(144)
turtle.forward(length)
turtle.right(144)
turtle.forward(length)
turtle.right(144)
turtle.forward(length)
turtle.right(144)
turtle.forward(length)
turtle.done()

print("\n#No.4\n")
import turtle
radius=int(input("Enter the radius of the ring : "))
separation=radius/5
turtle.goto(0,0)
turtle.left(90)
turtle.color("blue")
turtle.circle(radius)
turtle.penup()
turtle.goto((2*radius)+separation,0)
turtle.pendown()
turtle.color("black")
turtle.circle(radius)
turtle.penup()
turtle.goto((4*radius)+(2*separation),0)
turtle.pendown()
turtle.color("red")
turtle.circle(radius)
turtle.penup()
turtle.goto(radius+(separation/2), -separation-radius)
turtle.pendown()
turtle.color("yellow")
turtle.circle(radius)
turtle.penup()
turtle.goto((3*radius)+(separation/2)+separation, -separation-radius)
turtle.pendown()
turtle.color("green")
turtle.circle(radius)
turtle.done()

print("\n#No.5\n")
import turtle
print("For first point p1")
x1=float(input("\tx : "))
y1=float(input("\ty : "))

print("For second point p2")
x2=float(input("\tx : "))
y2=float(input("\ty : "))

print("For third point p3")
x3=float(input("\tx : "))
y3=float(input("\ty : "))

area=round(0.5*abs((x1*(y2-y3))+(x2*(y3-y1))+(x3*(y1-y2))), 2)

turtle.penup()
turtle.goto(x1-25,y1)
turtle.color("blue")
turtle.write(f"x1:{x1} , y1: {y1}")
turtle.color("black")
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.penup()
turtle.goto(x2-25,y2)
turtle.color("blue")
turtle.write(f"x2:{x2} , y2: {y2}")
turtle.color("black")
turtle.goto(x2,y2)
turtle.pendown()
turtle.goto(x3,y3)
turtle.penup()
turtle.goto(x3,y3+3)
turtle.color("blue")
turtle.write(f"x3:{x3} , y3: {y3}")
turtle.color("black")
turtle.goto(x3,y3)
turtle.pendown()
turtle.goto(x1,y1)
turtle.penup()
turtle.goto(x1,y1-15)
turtle.color("green")
turtle.write(f"Area is {area} square unit")
turtle.color("black")
turtle.goto(x1,y1)
turtle.done()

