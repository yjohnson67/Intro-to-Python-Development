import csv
import random
import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # skip the headers
        dictionary = {}
        for row in reader:
            key = row[key_column_index]
            value = row
            dictionary[key] = value
    return dictionary

def main():
    # Call read_dictionary to load products.csv
    products_dict = read_dictionary('products.csv', 0)
    # Print the dictionary
    print("Store Name: ABC Store")
    print("Date: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    print("Ordered Items")
    total_items = 0
    subtotal = 0
    # Keep track of the products ordered
    ordered_products = []
    # Open the request.csv file
    with open('request.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the headers
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            if product_number in products_dict:
                product = products_dict[product_number]
                product_name = product[1]
                product_price = float(product[2])
                total_price = product_price * quantity
                ordered_products.extend([product_name] * quantity)
                print(f"{product_name}: {quantity} @ ${product_price:.2f} = ${total_price:.2f}")
                total_items += quantity
                subtotal += total_price
            else:
                print(f"Product {product_number} not found.")
    print(f"\nTotal Items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    # Compute the sales tax amount
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    print(f"Sales Tax (6%): ${sales_tax:.2f}")
    # Compute the total amount due
    total = subtotal + sales_tax
    print(f"Total: ${total:.2f}")
    # Print a thank you message
    print("\nThank you for shopping at ABC Store!")
    # Print a coupon
    if ordered_products:
        random_product = random.choice(ordered_products)
        print(f"\nHere's a coupon for your next purchase: Buy one {random_product}, get one free!")

if __name__ == '__main__':
    main()
    