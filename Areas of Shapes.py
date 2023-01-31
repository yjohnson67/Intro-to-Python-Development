#Square-The area is the length of a side squared.
#Area of a square = Side x Side 
import math
def area_square(n):
    area = pow(n,2)
    return area
num=float(input("What is the length of a side of the square? " ))
print("The area of the square is=",area_square(num))
print()

#Rectangle - The area is the length multiplied by the width
#Area of a rectangle = Width * Height
def area_rectangle (width, height):
    area = (width*height)
    return area
width=float(input("What is the width of the rectangle? "))
height=float(input("What is the height of the retancle? "))
print("The area of the retancle is=",area_rectangle(width,height))
print()

#Circle- The area is Pi (you can use 3.14) multiplied by the radius squared.
radius=float(input("What is the radius of the circle? "))
area = math.pi * (radius ** 2)
print(f"The area of the circle is:  {area:.3f}")




