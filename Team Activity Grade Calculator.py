grade_input = float(input("What is the percentage of your grade? "))
print()
if grade_input >= 90:
    letter = "A"
elif grade_input  >= 80:
    letter = "B"
elif grade_input  >= 70:
    letter = "C"
elif grade_input  >= 60:
    letter = "D"
else:
    letter = "F"    

#print(f"Your grade is: {letter}")

#if grade_input >= 70:
 #   print("Congratulations!  You are passing!")
#else: 
 #   print("You are not passing, please try harder. I know you can do this!")


# Stretch Challenge 1
sign = ""

last_digit = grade_input % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Stretch Challenge 2
if grade_input >= 93:
    sign = ""

# Stretch Challenge 3
if letter == "F":
    sign = ""

print(f"Your letter grade is: {letter}{sign}")

if grade_input >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")