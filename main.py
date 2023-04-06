# Area of Geometry

# import the math module first
import math

# creating trapezoid function to calculate the area
def Trapezoid():
    a_base = float(input("enter first base: "))
    b_base = float(input("enter second base: "))
    height = float(input("enter your height: "))

    area = (a_base + b_base) / 2 * (height / 1)
    print("area of a trapezoid is : ", area)

# creating parallelogram function to calculate the area
def parallelogram():
    height = float(input("enter your length: "))
    breath = float(input("enter your breath: "))
    area = height * breath
    print("the of the rectangle is : ", area)

# creating triangle function to calculate the area
def triangle():
    height = float(input("enter the height:"))
    base = float(input("enter your base: "))
    area = 1 / 2 * base * height
    print("the area of the triangle is : ", area)

# creating rectangle function to calculate the area
def rectangle():
    length = float(input("enter your length: "))
    breath = float(input("enter your breath: "))
    rec_area = length * breath
    print("the of the rectangle is : ", rec_area)

# creating circle function to calculate the area
def circle():
    radius = float(input("enter the radius: "))

    area = math.pi * (math.pow(radius, 2))
    print("the area of the circle is {:.2f}".format(area))

# function to get the shape
def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle()
    elif shape == "circle":
        circle()
    elif shape == "triangle":
        triangle()
    elif shape == "parallelogram":
        parallelogram()
    elif shape == "trapezoid":
        Trapezoid()
    else:
        print("this are the available one, which are \ncircle, rectangle, trinagle, trapezoid and parallelogram")


def main():
    shape_type = input("Get area of what shape: ")
    get_area(shape_type)


main()