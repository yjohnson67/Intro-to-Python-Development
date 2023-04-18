import math

# function to get user input for length and width
def get_length_and_width():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    return length, width

# function to calculate area of rectangle
def calculate_area(length, width):
    area = length * width
    return area

# function to calculate perimeter of rectangle
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

# function to display the results
def display_results(area, perimeter):
    print(f"The area of the rectangle is {area}.")
    print(f"The perimeter of the rectangle is {perimeter}.")

# main function
def main():
    length, width = get_length_and_width()
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    display_results(area, perimeter)

if __name__ == '__main__':
    main()