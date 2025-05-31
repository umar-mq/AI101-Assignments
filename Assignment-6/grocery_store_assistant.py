from utils import *

product_catalog = {}

def purchase():
    global product_catalog
    purchase = {"items": {}, "total": 0.0}

    while True:
        option = choose_option("Customer Purchase", ["Add Item", "Remove Item", "Display Reciept", "Exit"], "Choose an option: ")

        if option == "Add Item":
            print_with_clear("\033[1;31mAdd Item\033[0m")
            display_catalog()

            name = input("Enter product name to add: ")
            if name not in product_catalog:
                print(f"Product '{name}' does not exist in the catalog.")
                continue

            qty = int(input("Enter quantity to purchase: "))
            if qty > product_catalog[name][0]:
                print(f"Insufficient stock for '{name}'. Available quantity is {product_catalog[name][0]}.")
                continue

            purchase["items"][name] = purchase["items"].get(name, 0) + qty
            purchase["total"] += product_catalog[name][1] * qty
            product_catalog[name] = (product_catalog[name][0] - qty, product_catalog[name][1])
            print(f"Added {qty} of {name} to the purchase.")
            continue
        
        elif option == "Remove Item":
            print_with_clear("\033[1;31mRemove Item\033[0m")

            print("Current items in purchase:")
            for item, qty in purchase["items"].items():
                print(f"{item}: {qty}")

            name = input("Enter product name to remove: ")
            if name not in purchase["items"]:
                print(f"Product '{name}' is not in the purchase.")
                continue

            qty = int(input("Enter quantity to remove: "))
            if qty > purchase["items"][name]:
                print(f"Cannot remove more than {purchase['items'][name]} of '{name}'.")
                continue

            purchase["total"] -= product_catalog[name][1] * qty
            product_catalog[name] = (product_catalog[name][0] + qty, product_catalog[name][1])
            if qty == purchase["items"][name]:
                del purchase["items"][name]
            else:
                purchase["items"][name] -= qty
            print(f"Removed {qty} of {name} from the purchase.")
            continue

        elif option == "Display Reciept":
            print_with_clear("\033[1;31mPurchase Receipt\033[0m")
            print("Items purchased:")
            for item, qty in purchase["items"].items():
                print(f"{item}: {qty} @ Rs. {product_catalog[item][1]} each")
            print(f"Total: Rs. {purchase['total']:.2f}")
            input("Press Enter to continue...")
            continue

        elif option == "Exit":
            break

        else:
            print('Invalid input')
            

def display_catalog():
    global product_catalog

    if not product_catalog:
        print("No products available.")
        return

    print()
    for name, (qty, price) in product_catalog.items():
        print(f"{name}: Quantity = {qty}, Price = Rs. {price}")
    print()

def add_item():
    global product_catalog

    print_with_clear("\033[1;31mAdd New Item\033[0m")
    name = input("Enter product name: ")
    if name in product_catalog:
        print(f"Product '{name}' already exists in the catalog.")
        return

    qty = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))

    product_catalog[name] = (qty, price)
    print(f"Added {name} with quantity {qty} and price {price}.")

def update_item():
    global product_catalog

    print_with_clear("\033[1;31mUpdate Item\033[0m")
    display_catalog()

    name = input("Enter product name to update: ")
    if name not in product_catalog:
        print(f"Product '{name}' does not exist in the catalog.")
        return

    mode = choose_option("Update Mode", ["Quantity", "Price", "Both"], "Choose update mode: ")

    if mode == "Quantity":
        qty = int(input("Enter new quantity: "))
        price = product_catalog[name][1]

    elif mode == "Price":
        price = float(input("Enter new price: "))
        qty = product_catalog[name][0]
    else:
        qty = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))

    product_catalog[name] = (qty, price)
    print(f"Updated {name} to quantity {qty} and price {price}.")

def delete_item():
    global product_catalog

    print_with_clear("\033[1;31mDelete Item\033[0m")
    display_catalog()

    name = input("Enter product name to delete: ")
    if name not in product_catalog:
        print(f"Product '{name}' does not exist in the catalog.")
        return

    del product_catalog[name]
    print(f"Deleted product '{name}' from the catalog.")

while True:
    option = choose_option("Grocery Store Assistant", ["Purchase", "Add Item", "Update Item", "Delete Item", "Display Catalog", "Exit"], "Choose an option: ")

    if option == "Purchase":
        purchase()
    elif option == "Add Item":
        add_item()
    elif option == "Update Item":
        update_item()
    elif option == "Delete Item":
        delete_item()
    elif option == "Display Catalog":
        display_catalog()
        input('Press Enter to continue...')
    elif option == "Exit":
        print("Exiting the Grocery Store Assistant. Goodbye!")
        break
    else:
        print('Invalid input')