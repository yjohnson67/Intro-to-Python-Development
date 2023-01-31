child_meal = float(input("What is the price of a child's meal? $"))
adult_meal = float(input("What is the price of an adult's meal? $"))
drinks_soda = float(input("What is the price of a soda drink? $"))
appetizer_price = float(input("What is the price of the appetizer? $"))
soup_cup = float(input("What is the price of a cup of soup? $"))
soup_bowl = float(input("What is the price of a bowl of soup? $"))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
drinks = int(input("How many drinks would you like? "))
appetizer = int(input("How many appetizers you like? "))
soup_cups = int(input("How many cups of soup would you like? "))
soup_bowls = int(input("How many bowls of soup would you like? "))
tax = float(input("What is the sales tax rate? "))
print(1 * "\n")

meal_total = (child_meal * children) + (adult_meal * adults) + (soup_cups * soup_cup) + (soup_bowls * soup_bowl) + (drinks_soda * drinks) + (appetizer_price * appetizer)
print(f"Subtotal: ${meal_total}")
total = meal_total 
sales_tax = (meal_total*(tax/100.0))
print("Sales Tax: ${:.2f}" .format(sales_tax))

tip = (input("Would you like to give a tip? "))
if tip == "yes":
        percentage = int(input("What is the percentage you would like to pay? "))
        tip_amount = (float(total * percentage / 100))
        print(f"${tip_amount:.2f}")

else:
    tip_amount = 0.0

payment_due = meal_total + sales_tax + tip_amount
print("Payment due is ${:.2f}" .format (payment_due))
payment = float(input("How much are you paying? $"))
change = (payment - payment_due)
print("change: ${:.2f}".format(change))


