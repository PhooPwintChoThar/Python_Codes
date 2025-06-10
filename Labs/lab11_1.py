import math

class Point(object):
    def __init__(self, x=0.00, y=0.00):
        self.x=float(x)
        self.y=float(y)

    def printInfo(self):
        print(f"Position : {self.x} , {self.y}")

class Circle(Point):
    def __init__(self, x=0.00, y=0.00, radius=0.00):

        super().__init__(x,y)
        self.radius=float(radius)

    def area(self):

        return math.pi*self.radius*self.radius
    
    def printInfo(self):
        print(f"Position : {self.x}, {self.y} , Radius: {self.radius} , Area:{self.area()}")

        

circle=Circle(5,4,25)
circle.printInfo()