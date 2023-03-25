import math
from datetime import datetime

def main():
    # tire prices
    width = [185, 195, 205, 215]
    ratio = [50, 55, 60, 65]
    wheel_diameter = [14, 15, 16, 17]
    price = [69, 163, 105, 117]
    for x in range(len(price)):
        print(f"{width[x]},{ratio[x]},{wheel_diameter[x]}:{price[x]}")
    tire_width, aspect_ratio, diameter = request()
    volume_calculation(tire_width, aspect_ratio, diameter)
    time()
    tf = None
    while type(tf) is not type(int()):
        tf = purchase(width, ratio, wheel_diameter, price)
        if tf == False:
            break
    if tf != False:
        number()    
        print(f'Your total is ${tf}')
    print("Thank you for using our program.")

# prompt user for tire dimensions
def request():
    while True:
        try:
            width = float(input("Enter the width of the tire in mm: "))
            aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
            diameter = float(input("Enter the diameter of the wheel in inches: "))
            if width <= 0 or aspect_ratio <= 0 or diameter <= 0:
                raise ValueError
            break
        except ValueError:
            print("Input a number greater than 0 or a number.")
    return width, aspect_ratio, diameter

# calculate tire volume
def volume_calculation(width, aspect_ratio, diameter):
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    print("The approximate volume is", round(volume, 2), "liters")
    return None

# print current date
def time():
    date = datetime.now().strftime('%Y-%m-%d')
    print("Current date", date)

# check if user wants to buy tires
def purchase(width, ratio, wheel_diameter, price):
    buy = input("Do you want to buy tires? (yes/no): ")
    if buy.lower() == "yes" or buy.lower() == 'y':
        print("We have these tires in stock.")
        for i in range(len(width)):
            print(f"{i+1}. Width: {width[i]}mm, Aspect Ratio: {ratio[i]}, Wheel Diameter: {wheel_diameter[i]} inches, Price: ${price[i]}")
        request = input('Which tire do you want to buy? (first or second or third or fourth or quit)')
        if request.lower() == "quit":
            return False
        elif request.lower() == 'first'or request == '1':
            index = 1
        elif request.lower() == 'second'or request == '2':
            index = 2
        elif request.lower() == 'third'or request == '3':
            index = 3
        elif request.lower() == 'fourth'or request == '4':
            index = 4
        else:
            index = -1
        if index != -1:
            print(f"You have selected tire {index}: Width: {width[index-1]}mm, Aspect Ratio: {ratio[index-1]}, Wheel Diameter: {wheel_diameter[index-1]} inches, Price: ${price[index-1]}")
            #print(type(price[index-1]))
            return price[index-1]
        else:
            print("Invalid input. No tire selected.")
    elif buy.lower() == "no" or buy.lower() == 'n':
        return False
def number():
        phone_number = input("Please enter your phone number: ")
        area_code = phone_number[0:3]
        prefix = phone_number[3:6]
        line_number = phone_number[6:10]
        formatted_phone_number = f"({area_code}) {prefix}-{line_number}"
        print("Your phone number is:", formatted_phone_number)

main()