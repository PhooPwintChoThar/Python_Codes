import turtle

def RobotBattle():
    #robot list stores the list of robots in the battle

    robotList=[]

    while True:
        #Clear the screen and draw the robots
        
        if robotList!=None:
            turtle.reset()
            i=0
            for robot in robotList:
                robot.draw() 
                turtle.write(i)
                i+=1

    
        #Display the status of each robot
        print("====Robots====")     
        i=0
        for robot in robotList:
            print(i,":", robot.displayStatus())
            i+=1
        print("==============")

        #Ask user which robot to command or to create a new robot
        choice=input("Enter which robot to order, 'c' to create new robot, 'q' to quit : ")
        if choice=="q":
            print("Game Ended.")
            break
        elif choice=='c':
            print("Enter which type of robots to create")
            robotType=input("'r' for Robot, 'm' for medical bot,'s' for Striker Bot : ")
            if robotType=='r':
                newRobot=Robot()
            elif robotType=='m':
                newRobot=MedicBot()
            elif robotType=='s':
                newRobot=StrikerBot()
            robotList.append(newRobot)
        else:
            n=int(choice)
            if n<0 or n>len(robotList)-1:
                print("Out of range")
                continue
            robotList[n].command(robotList)

        #Delete all robots with  health <=0 from the list
        i=0
        for robot in robotList:
            if (robot.health <=0):
                robotList.remove(robotList[i])
            i+=1
    
class Robot(object):
    def __init__(self):
        self.x=0
        self.y=0
        self.health=100
        self.energy=100

    def move(self, x, y):
        if self.energy>0:
            self.x=x
            self.y=y
            self.energy-=10

    def draw(self):
        turtle.speed(0)
        self.radius=50
        turtle.penup()
        turtle.goto(self.x, self.y-self.radius)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()
        turtle.goto(self.x,self.y)
        if isinstance(self, MedicBot):
            turtle.left(90)
            turtle.forward(5)
            turtle.right(90)
            turtle.forward(5)
            turtle.pendown()
            for i in range (4):
                turtle.forward(35)
                turtle.right(90)
                turtle.forward(10)
                turtle.right(90)
                turtle.forward(35)
                turtle.left(90)
            turtle.penup()
            turtle.goto(self.x, self.y)
        elif isinstance(self, StrikerBot):
            turtle.left(90)
            turtle.forward(40)
            turtle.right(135)
            turtle.pendown()
            for i in range(4):
                turtle.forward(40*2**(1/2))
                turtle.right(90)
            turtle.left(45)
            turtle.penup()
            turtle.goto(self.x, self.y)
    def displayStatus(self):
        return f"x={self.x}, y={self.y}, health={self.health}, energy={self.energy}"

    def command(self, robotList):
        print("Possible actions : move")
        newX=int(input("Enter new x coordinate: "))
        newY=int(input("Enter new y coordinate: "))
        self.move(newX , newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):
        distance=((self.x-r.x)**2+(self.y-r.y)**2)**(1/2)
        if self.energy>=20 and distance<=(2*self.radius+10):
            self.energy-=20
            r.health+=10
        else:
             print("Enegy less than 20 or distance less than 10")

    def command(self, robotList):
        commandForMR=input("Choose to take action, 'm' to move, 'h' to heal another robot : ")
        if commandForMR=='m':
            newX=int(input("Enter new x coordinate: "))
            newY=int(input("Enter new y coordinate: "))
            super().move(newX , newY)
        elif commandForMR=='h':
            robotToHeal=int(input("Which robot you want to heal?  : "))
            while robotToHeal<0 or robotToHeal>len(robotList)-1:
                robotToHeal=int(input("Out of range!Which robot you want to heal? : "))
            self.heal(robotList[robotToHeal])
        else:
            print("invalid input")
        

           
    
class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile=5

    def strike(self, r):
        distance=((self.x-r.x)**2+(self.y-r.y)**2)**(1/2)
        if self.energy>=20 and self.missile>0 and distance<=(2*self.radius+10):
            self.energy-=20
            self.missile-=1
            r.health-=50
        else:
            print("Enegy less than 20 or distance less than 10 or missle less than 0")

    def displayStatus(self):
        return f"x={self.x} , y={self.y} , Energy={self.energy} , Health={self.health} , Missle={self.missile}"

    
    def command(self, robotList):
        commandForSR=input("Choose to take action, 'm' to move, 's' to strike another robot : ")
        if commandForSR=='m':
            newX=int(input("Enter new x coordinate: "))
            newY=int(input("Enter new y coordinate: "))
            super().move(newX , newY)
        elif commandForSR=='s':
            robotToStrike=int(input("Which robot you want to strike? : "))
            while robotToStrike<0 or robotToStrike>len(robotList)-1:
                robotToStrike=int(input("Out of range!Which robot you want to strike? : "))
            self.strike(robotList[robotToStrike])
        else:
            print("invalid input")


RobotBattle()
turtle.done()





