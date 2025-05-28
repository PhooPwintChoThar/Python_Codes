#No.1
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

#No.2
def bubble_sort(inputList):
    list=[]
    list.extend(inputList)
    anySort=True

    while anySort:
        anySort=False
        for number in range(len(list)-1):
            if list[number]>list[number+1]:
                temp=list[number+1]
                list[number+1]=list[number]
                list[number]=temp
                anySort=True
            
    return list

print(bubble_sort([3,2,9,7,8]))

#No.3
def my_union(list1,list2):
    union=[]
    union.extend(list1)
    for y in list2:
        if y in union:
            continue
        else:
            union.append(y)
    
    
    return (union)


def my_intersection(list1,list2):
    same=[]
    for x in list1:
        for y in list2:
            if y==x and x not in same:
                #print("append",x)
                same.append(x)
                break
            else:
                continue

    return same

def my_difference(list1,list2):
    difference=[]
    for x in list1:
       if x in list2:
           continue
       else:
           difference.append(x)
    return difference

list1=[3,1,2,7]
list2=[4,1,2,5]

list3=my_union(list1, list2)
print(list3)

list4=my_intersection(list1, list2)
print(list4)

list5=my_difference(list1, list2)
print(list5)

#No.4
def print_table(list):
    longestLengths = []
    for i in range(len(list[0])):
        tempLength = 0
        for j in range(len(list)):
            tempString = str(list[j][i])
            if len(tempString) > tempLength:
                tempLength = len(tempString)
        longestLengths.append(tempLength)

    for x in range(len(list)):
        for y in range(len(list[0])):
            strLength = longestLengths[y]+3
            print(f"{str(list[x][y]):{strLength}s}", end=" ")
        print()


print_table([["X","Y"],[0,0],[10,10],[200,200]])

print("\n\n")

print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
])

print("\n\n")

print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido van Rossum the Creator of Python", "van Rossum"],
    ["002", "Donald Knuth the Author of The Art of Computer Programming", "Knuth"],
    ["003", "Gordon Moore the Co-founder of Intel Corporation", "Moore"],
    ["004", "Grace Hopper the Pioneer of Computer Programming", "Hopper"]
])

#No.5
def isAnagram(str1,str2):

    if len(str1)!=len(str2):
        return f"{str1} and {str2} are not anagrams."
    else:
        check1=[]
        check1.extend(str1)
        check2=[]
        check2.extend(str2)

        for x in check1:
            for y in check2:
                if y==x:
                    check2.remove(y)

        if len(check2)==0:
            return f"{str1} and {str2} are  anagrams."
        else:
            return f"{str1} and {str2} are not anagrams."


print(isAnagram("silent", "listen"))  
print(isAnagram("triangle", "integral"))  
print(isAnagram("apple", "papel"))  
print(isAnagram("evil", "vile"))  
print(isAnagram("fluster", "restful"))  
print(isAnagram("abcd", "dcba")) 
print(isAnagram("rat", "car"))  
print(isAnagram("hello", "world"))  
