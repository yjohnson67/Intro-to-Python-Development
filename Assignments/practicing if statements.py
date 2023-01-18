#Practicing if statements with values of numbers
firstNum = int(input("What is the first number? "))
secondNum = int(input("What is the second number? "))

if firstNum > secondNum:
    print("The first number is greater")
else:
    print("The first number is not greater")

if firstNum == secondNum:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if secondNum > firstNum:
    print("The second number is greater")
else:
    print("The second number is not greater")

print() #blank line

user_animal = input("What is your favorite animal? ")

if user_animal.lower() == "bear":
    print("That's my favorite animal too!")
else:
    print("That one if not my favorite.")