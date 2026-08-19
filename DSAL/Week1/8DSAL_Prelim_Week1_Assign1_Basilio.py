print("=" * 30)
print("Grocery List Maker")
print("=" * 30)

grocery_list = []
user_input = 99

while True:
    user_input = input("Enter item to add to the list (0 to exit): ")
    
    if user_input == "0":
        break
    
    if not user_input.strip():
        print("Enter a valid item.")
        continue

    grocery_list.append(user_input.lower())

grocery_list.sort()

def display_list(given_list):
    print("=" * 30)
    for index, item in enumerate(given_list, 1):
        print(index, ": ", item.capitalize())
    print("=" * 30)

print()
print("Your grocery list:")
display_list(grocery_list)

while True:
    print("")
    print("Select action:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Change Item")
    print("4. Display Grocery List")
    print("5. Exit")

    while True:
        try:
            user_action = int(input("Action: "))
            break
        except ValueError as ve:
            print("Please input numbers only.")

    match (user_action):
        case 1:
            while True:
                to_add = input("Enter item to add: ").lower()
                grocery_list.sort()
                if not to_add.strip():
                    print("Error. Enter valid item.")
                else:
                    break

            grocery_list.append(to_add)
        case 2:
            to_remove = input("Enter item to remove: ").lower()
            if to_remove in grocery_list:
                grocery_list.remove(to_remove)
            else:
                print("Could not find item to remove.")
        case 3:

            to_change = input("Enter item to change: ").lower()
            
            if to_change in grocery_list:
                while True:
                    new_item = input("Enter new item: ").lower()
                    if not new_item.strip():
                        print("Error input valid item.")
                    else:
                        break

                item_to_change = grocery_list.index(to_change)
                grocery_list[item_to_change] = new_item
                grocery_list.sort()

        case 4:
            display_list(grocery_list)
        case 5:
            break
        case _:
            print("Error invalid action.")

print("Code by: Ned Markus S. Basilio | CS-201")