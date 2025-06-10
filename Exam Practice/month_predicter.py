sum=0
question1=int(input("Is your birth month in Set1?\n"+\
                    "1  3  5  7  9  11\n"))
if question1==1:
    sum+=1

question2=int(input("Is your birth month in Set2?\n"+\
                    "2  3  6  7  10  11\n"))

if question2==1:
    sum+=2

question3=int(input("Is your birth month in Set3?\n"+\
                    "4  5  6  7  12  \n"))

if question3==1:
    sum+=4

question4=int(input("Is your birth month in Set1?\n"+\
                    "8 9 10 11 12  \n"))

if question4==1:
    sum+=8

print("Your birth month is " , sum)