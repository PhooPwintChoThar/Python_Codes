import turtle
from abc import ABC, abstractmethod

class Char(ABC):
    @abstractmethod
    def draw(self, x, y):
        pass
    
    @abstractmethod
    def getWidth(self):
        pass

class Char0(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
    
    def getWidth(self):
        return 20

class Char1(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(40)
        turtle.left(135)
        turtle.forward(10)
        turtle.right(225)
        turtle.penup()
    
    def getWidth(self):
        return 10

class Char2(Char):
    def draw(self, x, y):
        turtle.goto(x, y)
        turtle.pendown()
        turtle.backward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(180)
        turtle.penup()
    
    def getWidth(self):
        return 20

class Char3(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.backward(20)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(180)
        turtle.penup()
    
    def getWidth(self):
        return 20

class Char4(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(20)
        turtle.left(90)
        turtle.pendown()
        turtle.forward(20)
        turtle.left(90)
        turtle.penup() 
   
    
    def getWidth(self):
        return 20

class Char5(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y + 40)
        turtle.pendown()
        turtle.left(180)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(180)
    
    def getWidth(self):
        return 20

class Char6(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y + 40)
        turtle.pendown()
        turtle.left(180)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
    
    def getWidth(self):
        return 20

class Char7(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(180)
    
    def getWidth(self):
        return 20

class Char8(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.backward(20)
    
    def getWidth(self):
        return 20

class Char9(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)

    
    def getWidth(self):
        return 20

def drawNum(x):
    char_dict = {
        '0': Char0(), '1': Char1(), '2': Char2(), '3': Char3(), '4': Char4(),
        '5': Char5(), '6': Char6(), '7': Char7(), '8': Char8(), '9': Char9()
    }
    
    #if isinstance(x, int):
    x = str(x)
    
    current_x = 0
    for digit in x:
        if digit in char_dict:
            char_obj = char_dict[digit]
            char_obj.draw(current_x, 0)
            current_x += char_obj.getWidth() + 20  
            
    
    turtle.done()  

# Example usage:
drawNum(12345678910)
