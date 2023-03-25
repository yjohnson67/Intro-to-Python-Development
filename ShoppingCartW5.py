def menu():
    shopping_cart = {}
    while True:
        print("Welcome to the Shopping Cart Program!")
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        choice = int(input("Please enter an action: "))

        if choice == 1:
            item = input("What item would you like to add? ")
            price = float(input(f"What is the price of '{item}'? "))
            shopping_cart[item] = price
            print(f"'{item}' has been added to the cart.")
        elif choice == 2:
            print("The contents of the shopping cart are:")
            for i, (item, price) in enumerate(shopping_cart.items(), 1):
                print(f"{i}. {item} - ${price:.2f}")
        elif choice == 3:
            item = int(input("Which item would you like to remove? "))
            item_removed = False
            for i, (key, value) in enumerate(shopping_cart.items(), 1):
                if i == item:
                    del shopping_cart[key]
                    item_removed = True
                    break
            if item_removed:
                print("Item removed.")
            else:
                print("Item not found.")
        elif choice == 4:
            total = sum(shopping_cart.values())
            print(f"The total price of the items in the shopping cart is ${total:.2f}")
        elif choice == 5:
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")

menu()