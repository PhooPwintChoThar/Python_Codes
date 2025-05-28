#No.1
def IntegerToBinary(integer):
    RAnswer=""
    dividend=integer
    divisor=2
    while dividend!=1:
        RAnswer+=str(dividend%divisor)
        dividend=dividend//divisor
    RAnswer+="1"
    return RAnswer[::-1]

def BinaryToInteger(binary):
    reverse=binary[::-1]
    integer=0
    for power in range(len(reverse)):
        integer+=int(reverse[power])*2**power
    return integer

def main():
   while True:
        integer=int(input(" Type an integer : "))
        if integer==0:
            print("It is 0.")
            break
        elif integer<0:
            print("It is negative.")
            break
        else:
            binary=IntegerToBinary(integer)
            decimal=BinaryToInteger(binary)
            print("The binary value of ",integer," is : " ,binary)
            print("Converting the binary of ",integer," is the same with ", integer," ? : ", decimal==integer)
main()


#No.2
text=input("Enter some text : ")
check=''
for c in text:
    if c in check:
        continue
    else:
        check+=c

for a in check:
    count=0
    for b in text:
        if b==a:
            count+=1
        else:
            continue
    print(f"{a}\t{(count/len(text)):>7.2%}")


#No.3
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


#No.4
BookNumber=input("Enter the first 9 digits of an ISBN-10 as a string : ")
while len(BookNumber)!=9 or BookNumber[0]!="0" :
    BookNumber=input("Invalid!\nEnter the first 9 digits of an ISBN-10 as a string : ")

checksum=0
for i in range(1,10):
    checksum+=int(BookNumber[i-1])*i
checksum%=11

if checksum==10:
    BookNumber+="X"
else:
    BookNumber+=str(checksum)

print("Your ISBN-10 number is : ",BookNumber)
