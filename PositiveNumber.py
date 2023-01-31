number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please enter a positive number. "))

print(f"Your number is: {number} ")