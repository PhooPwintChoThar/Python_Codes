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