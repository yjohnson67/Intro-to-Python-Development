f_name = input("What is your first name? ")
l_name = input("What is your last name? ")
title = input("What is your job title? ")
idnum = input("What is your id number? ")
email = input("What is your email? ")
phone = input("What is your phone number? ")
hair = input("What is your hair color? ")
birth = input("What month were your born? ")
eye = input("What color are your eyes? ")
training = input("Have your received your training? ")


print("Please enter the following information for your ID card: ")
print("---------------------------------------------------------")
print(f"{l_name.upper()}, {f_name.capitalize()}")
print(title.capitalize())
print(f"ID: {idnum}")
print()
print(email)
print(f"({phone[:3]}){phone[3:6]}-{phone[6:]}")
print()
print(f"hair:  {hair.capitalize():12} Eyes: {eye.capitalize()}")
print(f"Month: {birth.capitalize():12} Training: {training.capitalize()}")
print("---------------------------------------------------------")