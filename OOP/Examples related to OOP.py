
#todo Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius
circle1 = Circle(4)

print(circle1.area())
print(circle1.perimeter())

#todo Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name= name
        self.country = country
        self.date_of_birth = date_of_birth

    def calcuate_age(self):
        return 2024 - self.date_of_birth
    
person = Person("a","g" , 2000)
print(person.calcuate_age())

#todo Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2
    
    def subtract(self):
        return self.n1 - self.n2
    
    def multiply(self):
        return self.n1 * self.n2
    
    def divide(self):
        try:
            return self.n1/self.n2
        except:
            print("Cannot divede by zero")

calculate1 = Calculator(2,1)
print(calculate1.multiply())


#todo Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like 
#todo circle, triangle(ucgen), and Rectangle
import math
class Shape:
    def calculateArea(self):
        pass

    def calculatePerimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def calculateArea(self):
        return math.pi * (self.radius ** 2)
    
    def  calculatePerimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.l=length
        self.w=width

    def calculateArea(self):
        return self.l*self.w
    
    def calculatePerimeter(self):
        return 2*(self.l + self.w)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculateArea(self):
        return 0.5 * self.base * self.height

    def calculatePerimeter(self):
        return self.side1 +  self.side2 + self.side3

#todo bir noktanın orjinden uzaklığını hesapla

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distanceFromOrigin(self):
        return (self.x*self.x + self.y*self.y) ** 0.5
    
    def distanceFromPoint(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2) ** 0.5
    
    def reflect_x (self):
        return (self.x , -(self.y))
    
    def slope_from_origin(self):
        try:
            return self.y/self.x
        except ZeroDivisionError:
            print("cannot divide by zero")

    def get_line_to(self,x1,y1):
        m = (self.y - y1) / (self.x - x1)
        return (m , y1 - (m*x1))
    
    def move(self, dx, dy):
        self.x = self.x + dx 
        self.y = self.y + dy

    def __str__(self):
        return str(self.x) + ", " + str(self.y)
    
    def mid(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return mx,my


p = Point(3,4)
q = Point(7,8)

midway = p.mid(q)
print(midway)

distance = p.distanceFromPoint(q)
print(distance)

#! __str__ ne işe yarıyor
p.move(5,4)
print(p)


point1 = Point(4,11)
print(point1.get_line_to(6, 15))