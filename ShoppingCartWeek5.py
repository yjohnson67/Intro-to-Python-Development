shopping_cart = []

#adding an item to the cart
def add_item():
    item_name = input("What item would you like to add? ")
    item_price = float(input("What is the price of '{}'? ".format(item_name)))
    shopping_cart.append((item_name, item_price))
    print("'{}' has been added to the cart.".format(item_name))

#viewing the item(s) that are in the cart
def view_cart():
    if not shopping_cart:
        print("The cart is empty.")
        return
    print("The contents of the shopping cart are:")
    #price of the item added to the cart
    for i, (item_name, item_price) in enumerate(shopping_cart):
        print("{}. {} - ${:.2f}".format(i + 1, item_name, item_price))

#removing the item(s) from the cart
def remove_item():
    view_cart()
    if not shopping_cart:
        return
    item_index = int(input("Which item would you like to remove? ")) - 1
    removed_item = shopping_cart.pop(item_index)
    print("Item removed.")

#total for all the items that are in the cart
def compute_total():
    if not shopping_cart:
        print("The cart is empty.")
        return
    total_price = sum(item_price for item_name, item_price in shopping_cart)
    print("The total price of the items in the shopping cart is ${:.2f}".format(total_price))

#if user would like to quit
def quit_program():
    print("Thank you. Goodbye.")
    exit()

#variables
actions = {
    1: add_item,
    2: view_cart,
    3: remove_item,
    4: compute_total,
    5: quit_program
}

#options for user to select
while True:
    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    choice = int(input("Please enter an action: "))
    actions[choice]()