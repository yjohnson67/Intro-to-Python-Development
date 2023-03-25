shopping_list = []
print("Please enter the items of the shopping list (type: quit to finish):")
while True:
    #adding items to the list until user types quit
    item = input("Item: ")
    if item == "quit":
        break
    shopping_list.append(item)

#display of items in the list
print("The shopping list is:")
for item in shopping_list:
    print(item)

print("The shopping list with indexes is:")
for i, item in enumerate(shopping_list):
    print(f"{i}. {item}")

#Changing the item the user picks
def update_item(lst):
    item_index = int(input("Which item would you like to change? "))
    new_item = input("What is the new item? ")
    lst[item_index] = new_item
    #printing the list with the changed item
    print("The updated shopping list with indexes is:")
    for i, item in enumerate(lst):
        print(f"{i}. {item}")

update_item(shopping_list)