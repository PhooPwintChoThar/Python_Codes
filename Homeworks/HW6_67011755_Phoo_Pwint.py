#1
def convertTime(hr):
    if hr>=0 and hr<=11 :
        zone="AM"
    elif hr>=12 and hr<=23:
        zone="PM"
    else:
        zone="Invalid time"
    if hr==12 or hr==0:
        return 12,zone
    else:
       return hr%12,zone

def main():
    hours=0
    minutes=33
    hour,zone_time=convertTime(hours)
    print(f"time24hourTo12hour(\"{hours}:{minutes}\")=> \"{hour:02}:{minutes:02} {zone_time}\"")

main()


#2

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
calenderMonth(8)

#4
def numToString(num):
    if num==1:
        return "one"
    elif num==2:
        return "two"
    elif num==3:
        return "three"
    elif num==4:
        return "four"
    elif num==5:
        return "five"
    elif num==6:
        return "six"
    elif num==7:
        return "seven"
    elif num==8:
        return "eight"
    elif num==9:
        return "nine"

def aboveTen(num):
    if num==11:
        return "eleven"
    elif num==12:
        return "twelve"
    elif num==13:
        return "thirteen"
    elif num==14:
        return "fourteen"
    elif num==15:
        return "fifteen"
    elif num==16:
        return "sixteen"
    elif num==17:
        return "seventeen"
    elif num==18:
        return "eighteen"
    elif num==19:
        return "nighteem"

def aboveTwenty(num):
    if num==2:
        return "twenty"
    elif num==3:
        return "thirty"
    elif num==4:
        return "forty"
    elif num==5:
        return "fifty"
    elif num==6:
        return "sixty"
    elif num==7:
        return "seventy"
    elif num==8:
        return "eighty"
    elif num==9:
        return "nighty"
    
def checkTwoDigit(num1,num2):
     integer=num1*10+num2
     if integer==10:
        return " ten "
     elif integer>10 and integer<20:
        return aboveTen(integer)
     else:
         second=aboveTwenty(num1)
         third=numToString(num2)
         return second+"-"+third

def main():
    integer=int(input("Type an integer between 0 and 999  : "))
    if integer>=0 and integer<=999:
        num=str(integer)
        i=len(num)
        if i==3:
            thirdDigit=numToString(int(num[0]))
            lastTwoDigit=checkTwoDigit(int(num[1]),int(num[2]))
            label=thirdDigit+" hundred and "+lastTwoDigit
        elif i==2:
            label=checkTwoDigit(int(num[0]),int(num[1]))
        else:
            label=numToString(integer)
        print(label)
    else:
        print("I don't know")

main()

#5
oneTNote=0
fiveHNote=0
oneHNote=0
fiftyNote=0
twentyNote=0
twoNote=0
oneNote=0
baht=int(input("Input your amount of money  :  "))
if baht>=1000:
    oneTNote=baht//1000
    hundred=baht%1000
    fiveHNote=hundred//500
    lessThanFiveH=hundred%500
    oneHNote=lessThanFiveH//100
    lessThanOneH=lessThanFiveH%100
    fiftyNote=lessThanOneH//50
    lessThanFifty=lessThanOneH%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=500:
    fiveHNote=baht//500
    lessThanFiveH=baht%500
    oneHNote=lessThanFiveH//100
    lessThanOneH=lessThanFiveH%100
    fiftyNote=lessThanOneH//50
    lessThanFifty=lessThanOneH%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=100:
    oneHNote=baht//100
    lessThanOneH=baht%100
    fiftyNote=lessThanOneH//50
    lessThanFifty=lessThanOneH%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=50:
    fiftyNote=baht//50
    lessThanFifty=baht%50
    twentyNote=lessThanFifty//20
    lessThanTwenty=lessThanFifty%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>=20:
    twentyNote=baht//20
    lessThanTwenty=baht%20
    twoNote=lessThanTwenty//2
    oneNote=lessThanTwenty%2
elif baht>0:
    twoNote=baht//2
    oneNote=baht%2
else:
    print("Invalid amount")

print("1000-Baht notes: ",oneTNote)
print("500-Baht notes: ",fiveHNote)
print("100-Baht notes: ",oneHNote)
print("50-Baht notes: ",fiftyNote)
print("20-Baht notes: ",twentyNote)
print("2-Baht coins: ",twoNote)
print("1-Baht coins: ",oneNote)

#6
def reverse (num):
    number=str(num)
    result=""
    for i in range(len(number)-1,-1,-1):
        result+=number[i]
    return int(result)

result=reverse(3456)
print("Reverse result is",result)

