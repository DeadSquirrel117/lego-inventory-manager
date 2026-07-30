from lego_item import LegoItem
command_ship = LegoItem("Craggers Command Ship", 70006, "Chima", "used", False, 80, 70) 
gorilla_striker = LegoItem("Gorzans Gorilla Striker", 70008, "Chima", "used", False, 50, 40)
inventory = []
inventory.append(command_ship)
inventory.append(gorilla_striker)





print("Lego Inventory Manager")

print("1. Add Item")
print("2. View Inventory")
print("3. View Total Value")
print("4. Search")
print("5. Delete Item")
print("6. Edit Item")
print("7. Exit")

while True:
    choice = int(input("Type one of the numbers: "))
    if choice == 1:
        set_name = input("Enter set name: ")
        set_number = int(input("Enter set number: "))
        theme = input("Enter theme: ")
        condition = input("Enter condition: ")
        complete = input("Is it complete? (yes or no): ").lower() == "yes"
        purchase_price = float(input("Enter price purchased for: "))
        estimated_value = float(input("Enter estimated value: "))
        new_item = LegoItem(set_name, set_number, theme, condition, complete, purchase_price, estimated_value)
        inventory.append(new_item)
        print("Added ", new_item.set_name, "to the inventory")
    elif choice == 2:
        for item in inventory:
            print("-------------------------")
            print(item)
            print("-------------------------")
    elif choice == 3:
        amount = 0
        for item in inventory:
            amount += item.estimated_value
        print("Total Estimated Value: $",amount)
    elif choice == 4:
        print("Search by:")
        print("1. Set Name:")
        print("2. Set Number:")
        print("3. Theme:")
        found = False
        search_choice = int(input("Choice: "))
        if search_choice == 1:
            set_search = input("Enter set Name: ")
            for item in inventory:
                if set_search.lower() in item.set_name.lower():
                    found = True
                    print("-------------------------")
                    print(item)
                    print("-------------------------")
        elif search_choice == 2:
            num_search = int(input("Enter set Number: "))
            for item in inventory:
                if num_search == item.set_number:
                    found = True
                    print("-------------------------")
                    print(item)
                    print("-------------------------")
        elif search_choice == 3:
            theme_search = input("Enter Theme: ")
            for item in inventory:
                if theme_search.lower() in item.theme.lower():
                    found = True
                    print("-------------------------")
                    print(item)
                    print("-------------------------")
        if found == False:
            print("Sorry I cant find anything for that")
    elif choice == 5:
        delete_num = int(input("Enter set number: "))
        found = False
        for item in inventory:
            if delete_num == item.set_number:
                found = True
                print("Deleted",item.set_name)
                inventory.remove(item)
        if not found:
                print("Set number not in Inventory")
    elif choice == 6:
        edit_num = int(input("Enter set number: "))
        found = False
        for item in inventory:
            if edit_num == item.set_number:
                found = True
                print("1. Condition")
                print("2. Purchase Price")
                print("3. Estimated Value")
                print("4. Complete")
                edit_choice = int(input("What item would you like to edit: "))
                if edit_choice == 1:
                    new_condition = input("Enter new Condition: ")
                    item.condition = new_condition
                    print("Condition Updated")
                    break
                elif edit_choice == 2:
                    new_price = float(input("Enter new Purchase Price: "))
                    item.purchase_price = new_price
                    print("Purcahse Price Updated")
                elif edit_choice == 3:
                    new_value = float(input("Enter new Estimated Value: "))
                    item.estimated_value = new_value
                    print("Estimated Value Updated")
                elif edit_choice == 4:
                    new_complete = input("Enter New Completion: ").lower()
                    item.complete = new_complete
                    print("Completion Updated")
        if not found:
            print("Cant find set number in inventory")
    elif choice == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1-4 .")