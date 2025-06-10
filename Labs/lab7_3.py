import turtle
class Rectangle:
    def __init__ (self, x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def getArea(self):
      return  self.width*self.height
    
    def getPerimeter(self):
       return 2*self.width+2*self.height
    
    def move(self,x,y):
       self.x=x
       self.y=y
       turtle.reset()
       turtle.penup()
       turtle.goto(x,y)
       turtle.pendown()

    def intersect(self,rec):
        width=self.width-abs(self.x-rec.x)
        height=self.height-abs(self.y-rec.y)
        return Rectangle(rec.x,rec.y,width,height)

    def draw(self):
       turtle.penup()
       turtle.goto(self.x,self.y)
       turtle.pendown()
       turtle.forward(self.width)
       turtle.right(90)
       turtle.forward(self.height)
       turtle.right(90)
       turtle.forward(self.width)
       turtle.right(90)
       turtle.forward(self.height)
       turtle.right(90)

yellow=Rectangle(80,50,100,120)
turtle.begin_fill()
turtle.fillcolor("yellow")
yellow.draw()
turtle.end_fill()
yellow.move(70,40)
turtle.begin_fill()
turtle.fillcolor("yellow")
yellow.draw()
turtle.end_fill()
blue=Rectangle(120,10,120,150)
turtle.begin_fill()
turtle.fillcolor("blue")
blue.draw()
turtle.end_fill()
intersect=yellow.intersect(blue)
turtle.begin_fill()
turtle.fillcolor("green")
intersect.draw()
turtle.end_fill()
turtle.done()


