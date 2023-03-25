import math
#calling the functions

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

#Beginning of program
shape = ""

#testing to see if the correct dementions are inputed for these shapes
while shape != "quit":
    shape = input("What is the shape (square, rectangle, circle, or quit): ")
    #determining if the shape is correct
    if shape == "quit":
        break   
    
   #area of the square
    elif shape == "square":
        side = int(input("Enter the length of the side of a square: "))
        result = compute_area_square(side)
        print("The area of the square is: ", result)

    #area of the rectangle
    elif shape == "rectangle":
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        result = compute_area_rectangle(length, width)
        print("The area of the rectangle is: ", result)
        
    #area of the circle
    elif shape == "circle":
        radius = int(input("Enter the radius of the circle: "))
        result = compute_area_circle(radius)
        print("The area of the circle is: ", result)
    else:
        print("Invalid shape.")
    