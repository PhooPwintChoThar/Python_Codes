#No.1
dictionary= {
    "b": "be",
    "cuz": "because",
    "cu": "see you",
    "c": "see",
    "da": "the",
    "ok": "okay",
    "r": "are",
    "u": "you",
    "w/o": "without",
    "y": "why",
    "8": "ate",
    "gr8": "great",
    "m8": "mate",
    "w8": "wait",
    "l8r": "later",
    "2mro": "tomorrow",
    "4": "for",
    "b4": "before",
    "1ce": "once",
    "&": "and",
    "ur": "your",
    "afaik": "as far as I know",
    "ASAP": "as soon as possible",
    "atm": "at the moment",
    "brb": "be right back",
    "btw": "by the way",
    "fyi": "for your information",
    "imho": "in my humble opinion",
    "imo": "in my opinion",
    "lol": "laugh out loud",
    "omg": "oh my god",
    "rofl": "roll on the floor laughing",
    "ttyl": "talk to you later"
}

def textese(s):
    
    string=s.split()
    for x in range(len(string)):
        for d in dictionary:
            if d==string[x]:
                string[x]=dictionary[d]
               
    new_string=""
    for s in string:
        new_string+=s+" "

    return new_string

def untextese(s):
    string=s
    for d in dictionary:
        if dictionary[d] in string:
            string=string.replace(dictionary[d], d)
    return string



print(textese("I will cu 2mro at da meeting"))
print(textese("Send me da document ASAP ."))
print(textese("w8 for me"))
print("\n\n")
print(untextese("I will see you tomorrow at the meeting "))
print(untextese("Send me the document as soon as possible . "))
print(untextese("wait for me."))


#No.2
def composite(dict1, dict2):
    composite={}
    for x in dict1:
        for y in dict2:
            if dict1[x]==y:
                composite[x]=dict2[y]

    return composite


dict1={'a':'p', 'b':'r', 'c':'q', 'd':'p',  'e':'s'}
dict2={'p':'1', 'q':'2', 'r':'3'}
print(composite(dict1, dict2))


#No.3
def product(sets): 
    items = [list(x) for x in sets] 

    def production(items):
        if len(items) == 2:
            result = []
            for first in items[0]:
                for second in items[1]:
                    result.append((first, second))
            return result
        else:
            other_product = production(items[1:])
            result = []
            for first in other_product:
                for second in items[0]:
                    result.append(first + (second,)) 
            return result

    if len(items) <= 1:
        result = [(x,) for x in items[0]]
        return set(result)
    else:
        result = production(items)  
        return set(result) 


s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])
result = product((s1, s2, s3))
print("Result is:\n", result)

#No.1
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
drawNum(12345678910)

#No.2
from abc import ABC, abstractmethod

class StationaryGood(ABC):
    @abstractmethod
    def get_cost(self):
        pass

class Magazine(StationaryGood):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_cost(self):
        return self.price

class Book(StationaryGood):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_cost(self):
        return self.price * 0.9 

class Ribbon(StationaryGood):
    def __init__(self, length):
        self.length = length
    
    def get_cost(self):
        return self.length * 5  

def getTotalCost(basket):
    return sum(item.get_cost() for item in basket)


basket = [
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Book("Windows 7 for Beginners", 200),
    Book("Windows 7 for Beginners", 200),
    Ribbon(10)
]

total_cost = getTotalCost(basket)
print(f"The total cost of the goods is: {total_cost} Bahts")


#No.3
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle2D:
    def __init__(self, center_x, center_y, width, height):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height

def getRectangle(points):
    if not points:
        return None
    
    min_x = min(point.x for point in points)
    max_x = max(point.x for point in points)
    min_y = min(point.y for point in points)
    max_y = max(point.y for point in points)
    
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    width = max_x - min_x
    height = max_y - min_y
    
    return Rectangle2D(center_x, center_y, width, height)


input=input("Enter the points as x1 y1 x2 y2 x3 y3 ... in one line:").split()
input_points=[float(x) for x in input]   
points = []
for i in range(0, len(input_points), 2):
    points.append(Point(input_points[i], input_points[i+1]))

bounding_rectangle = getRectangle(points)

if bounding_rectangle:
    print(f"The bounding rectangle is centered at ({bounding_rectangle.center_x:.1f}, {bounding_rectangle.center_y:.1f}) "
            f"with width {bounding_rectangle.width:.1f} and height {bounding_rectangle.height:.1f}")
else:
    print("No points were entered.")


turtle.penup()
turtle.goto(bounding_rectangle.center_x, bounding_rectangle.center_y)
turtle.forward(bounding_rectangle.width/2)
turtle.left(90)
turtle.forward(bounding_rectangle.height/2)
turtle.left(90)
turtle.pendown()
for i in range(2):
    turtle.forward(bounding_rectangle.width)
    turtle.left(90)
    turtle.forward(bounding_rectangle.height)
    turtle.left(90)
turtle.penup()
for p in points:
    turtle.goto(p.x, p.y)
    turtle.pendown()
    turtle.dot(6)
    turtle.penup()
    turtle.goto(bounding_rectangle.center_x, bounding_rectangle.center_y)
turtle.done()