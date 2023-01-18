first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
#capitalize function
print("Hello " + first_name.capitalize() + " " + last_name.capitalize())

#Custom String Formatting:
#output = "Hello, " + first_name + " " + last_name
#output = "Hello, {} {}" .format(first_name, last_name)
#output = "Hello, {0} {1} " .format(first_name, last_name)
#ONLY available in Python 3
#output = f"Hello, {first_name} {last_name}"