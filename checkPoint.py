age = int(input(f"How old are you? "))
next_year_age = + 1
#print(f"On your next birthday, you will be {next_year_age}.")
# We could do the addition right in the display if we choose to:
print(f"On your next birthday, you will be {age + 1}.")

print()

cartons = int(input("How many egg cartons do you have? "))
eggs = cartons *12
print(f"You have {eggs} eggs")

print()

cookies = int(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))
cookies_per_person = cookies / people

print(f"Each person may have {cookies_per_person} cookies")