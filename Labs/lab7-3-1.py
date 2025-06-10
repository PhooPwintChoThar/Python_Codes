import turtle

class Circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius

    def getArea(self):
        return self.radius*self.radius*3.14
    
    def getPerimeter(self):
        return 2*self.radius*3.14
    
    def move(self,x,y):
        turtle.reset()
        self.x=x
        self.y=y

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y-self.radius)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.write(f"{self.x},{self.y}")

circle=Circle(33,44,50)
circle.draw()
circle.move(11,46)
circle.draw()
turtle.done()