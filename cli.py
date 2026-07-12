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

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Feature coming next...")


menu()