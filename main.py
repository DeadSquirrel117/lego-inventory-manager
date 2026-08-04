import json
import os
from lego_item import LegoItem
from inventory import get_total_value, view_inventory
inventory = []
if os.path.exists("inventory.json"):

    with open("inventory.json", "r") as file:
        inventory_data = json.load(file)

    for item in inventory_data:
        lego_set = LegoItem(
            item["set_name"],
            item["set_number"],
            item["theme"],
            item["condition"],
            item["complete"],
            item["purchase_price"],
            item["estimated_value"]
        )

        inventory.append(lego_set)

    print("Inventory loaded successfully!")

else:
    print("No inventory file found.")
while True:
    print("Lego Inventory Manager")

    print("1. Add Item")
    print("2. View Inventory")
    print("3. View Total Value")
    print("4. Search")
    print("5. Delete Item")
    print("6. Edit Item")
    print("7. Exit")
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
        view_inventory(inventory)
    elif choice == 3:
        print("Total Estimated Value: $", get_total_value(inventory))
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
                    print(item)
                    break
                elif edit_choice == 2:
                    new_price = float(input("Enter new Purchase Price: "))
                    item.purchase_price = new_price
                    print("Purcahse Price Updated")
                    print(item)
                    break
                elif edit_choice == 3:
                    new_value = float(input("Enter new Estimated Value: "))
                    item.estimated_value = new_value
                    print("Estimated Value Updated")
                    print(item)
                    break
                elif edit_choice == 4:
                    new_complete = input("Enter New Completion: ").lower() == "yes"
                    item.complete = new_complete
                    print("Completion Updated")
                    print(item)
                    break
        if not found:
            print("Cant find set number in inventory")
    elif choice == 7:
        inventory_data = []
        for item in inventory:
            inventory_data.append(item.to_dict())
        with open("inventory.json", "w") as file:
            json.dump(inventory_data, file, indent=4)

        print("Inventory saved!")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1-4 .")