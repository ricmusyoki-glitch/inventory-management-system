import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():

    response = requests.get(f"{BASE_URL}/inventory")

    data = response.json()

    print("\nInventory Items:\n")

    for item in data:
        print(item)

    input("\nPress Enter to continue...")


def view_single_item():

    item_id = input("Enter item ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:

        print("\nItem Details:\n")
        print(response.json())

    else:

        print("\nItem not found.")

    input("\nPress Enter to continue...")


def add_item():

    name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    payload = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=payload
    )

    if response.status_code == 201:

        print("\nItem added successfully.")
        print(response.json())

    else:

        print("\nFailed to add item.")

    input("\nPress Enter to continue...")

def update_item():

    item_id = input("Enter item ID to update: ")

    quantity = int(input("New Quantity: "))

    payload = {
        "quantity": quantity
    }

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=payload
    )

    if response.status_code == 200:

        print("\nItem updated successfully.")
        print(response.json())

    else:

        print("\nItem not found.")

    input("\nPress Enter to continue...")

def delete_item():

    item_id = input("Enter item ID to delete: ")

    response = requests.delete(
        f"{BASE_URL}/inventory/{item_id}"
    )

    if response.status_code == 200:

        print("\nItem deleted successfully.")
        print(response.json())

    else:

        print("\nItem not found.")

    input("\nPress Enter to continue...")

def find_product():

    barcode = input("Enter barcode: ")

    response = requests.get(
        f"{BASE_URL}/product/{barcode}"
    )

    if response.status_code == 200:

        print("\nProduct Found:\n")
        print(response.json())

    else:

        print("\nProduct not found.")

    input("\nPress Enter to continue...")

def menu():

    while True:

        print("\n===== Inventory Management System =====")
        print("1. View Inventory")
        print("2. View Single Item")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Find Product From OpenFoodFacts")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_single_item()

        elif choice == "3":
            add_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            find_product()
         
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Feature coming next...")


menu()