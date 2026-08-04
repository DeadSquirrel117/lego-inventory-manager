def get_total_value(inventory):
    total = 0

    for item in inventory:
        total += item.estimated_value

    return total
def view_inventory(inventory):
    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    for item in inventory:
        print("-------------------------")
        print(item)
        print("-------------------------")