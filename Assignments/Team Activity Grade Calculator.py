#grade calculator to determine grades
grade = int(input("What is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

#Stretch Challenge
sign = ""
last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit >= 3:
    sign = "-"
else:
    sign = ""

#Stretch Challenge 2
if last_digit >= 93:
    sign = ""

#Stretch Challenge 3
if last_digit == "F":
    sign = ""

print(f"Your final grade is: {letter}{sign}")

if grade >= 70:
    print("You passed the class!  Congratulations!")
else:
    print("Persist, stay focused, move forward, don't be afraid to ask questions! Good luck with your next class!")