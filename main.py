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
print("5. Exit")

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
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1-4 .")