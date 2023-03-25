import datetime

# Get the current day of the week
now = datetime.datetime.now()
day_of_week = now.strftime("%A") #check the date
print(f"Today is {day_of_week}, {now}")

# Ask the user for prices and quantities and compute the subtotal
subtotal = 0
while True:
    price = float(input("Enter the price (0 to exit): $"))
    if price == 0:
        break
    quantity = int(input("Enter the quantity: "))
    subtotal += price * quantity

# Check if today is Tuesday or Wednesday and the subtotal is greater than $50
if day_of_week == "Tuesday" or day_of_week == "Wednesday":
    if subtotal > 50:
        # Apply the 10% discount
        discount_rate = 0.1
        discount = subtotal * discount_rate
        subtotal -= discount
        print(f"Discount applied: ${discount:.2f}")
    else:
        # Compute and print the additional amount needed to receive the discount
        difference = 50 - subtotal
        print(f"Add ${difference:.2f} to receive the discount.")

# Calculate the sales tax and total amount due
tax_rate = 0.06
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

# Print the results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total amount due: ${total:.2f}")