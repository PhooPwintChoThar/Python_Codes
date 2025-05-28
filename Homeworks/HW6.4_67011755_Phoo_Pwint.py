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
