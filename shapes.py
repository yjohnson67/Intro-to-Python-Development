import math
import pytest


def calculate_rectangle_area(length, width):
    return length * width


def calculate_triangle_area(base, height):
    return 0.5 * base * height


def calculate_circle_area(radius):
    return math.pi * radius ** 2


def calculate_area(shape, dimensions):
    if shape == "rectangle":
        return calculate_rectangle_area(dimensions[0], dimensions[1])
    elif shape == "triangle":
        return calculate_triangle_area(dimensions[0], dimensions[1])
    elif shape == "circle":
        return calculate_circle_area(dimensions[0])
    else:
        raise ValueError("Invalid shape entered.")


def get_dimensions(shape):
    if shape == "rectangle":
        length = input("Enter length: ")
        width = input("Enter width: ")
        return [float(length), float(width)]
    elif shape == "triangle":
        base = input("Enter base: ")
        height = input("Enter height: ")
        return [float(base), float(height)]
    elif shape == "circle":
        radius = input("Enter radius: ")
        return [float(radius)]
    else:
        raise ValueError("Invalid shape entered.")


def main():
    shape = input("Enter the name of the shape (rectangle, triangle, or circle): ")
    dimensions = get_dimensions(shape)

    area = calculate_area(shape, dimensions)

    print(f"The area of the {shape} is {area:.2f}")


if __name__ == '__main__':
    main()