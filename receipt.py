import csv
from datetime import datetime
import random

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
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "\n")
    print("Ordered Items")
    
    # Open the request.csv file
    with open('request.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the headers
        ordered_items =[]
        total_items = 0
        subtotal = 0
        for row in reader:
            product_number = row[0]
            quantity = int(row[1])
            if product_number in products_dict:
                product = products_dict[product_number]
                product_name = product[1]
                product_price = float(product[2])
                total_price = product_price * quantity
                ordered_items.append((product_name, quantity, total_price))
                print(f"{product_name}: {quantity} @ ${product_price:.2f} = ${total_price:.2f}")
                total_items += quantity
                subtotal += total_price
            else:
                print(f"Error: unknown product ID in the request.csv file 'R002'")
        
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total_due = subtotal + sales_tax
        
        print(f"\nTotal Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax (6%): ${sales_tax:.2f}")
        print(f"Total Due: ${total_due:.2f}")
        print("\nThank you for shopping at ABC Store!")
        print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        #Print a coupon for a random ordered item
        if ordered_items:
            item = random.choice(ordered_items)
            product_name = item[0]
            print(f"\nHere's a coupon for ${item[2]:.2f} off your next purchase of {product_name}!")
if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print("Error: missing file.\n[Errno 2] No such file or directlry: 'products.csv'")
    except PermissionError:
        print("Error: permission denied.")
    except KeyError:
        print("Error: invalid key.") 