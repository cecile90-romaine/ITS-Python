# Esercizio_5:
"""
Inventory Management System:

    Create a list to store the items in inventory.
    Create a function that defines an item with a code, name, quantity, and price.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops to manage the various inventory operations.

"""

from typing import Any

# Define the inventory as a list to store all items
inventory: list[dict[str, Any]] = []

# Function to define a new item with its details
def create_item(code: str, name: str, quantity: int, price: float) -> dict[str, Any]:
    return {
        "code": code,
        "name": name,
        "quantity": quantity,
        "price": price
    }

# Function to add a new item to the inventory
def add_item(item: dict[str, Any]) -> None:
    # Check if the item already exists (based on code)
    for existing_item in inventory:
        if existing_item["code"] == item["code"]:
            print(f"Item with code {item['code']} already exists.")
            return
    inventory.append(item)
    print(f"Item {item['name']} added successfully.")

# Function to remove an item from the inventory by its code
def remove_item(code: str) -> None:
    for item in inventory:
        if item["code"] == code:
            inventory.remove(item)
            print(f"Item with code {code} removed.")
            return
    print(f"Item with code {code} not found.")

# Function to search for an item by code
def search_item(code: str) -> dict[str, Any] | None:
    for item in inventory:
        if item["code"] == code:
            return item
    return None

# Function to update an existing item's quantity or price
def update_item(code: str, quantity: int = None, price: float = None) -> None:
    for item in inventory:
        if item["code"] == code:
            if quantity is not None:
                item["quantity"] = quantity
            if price is not None:
                item["price"] = price
            print(f"Item with code {code} updated.")
            return
    print(f"Item with code {code} not found.")

# Example usage
# Define items to be added
items_to_add: dict[str, Any] = [
    create_item("P001", "Monitor", 5, 150.00),
    create_item("P002", "Keyboard", 15, 30.00),
    create_item("P003", "Mouse", 25, 20.00),
]

# Add items
for item in items_to_add:
    add_item(item)

# Search items
items_to_search: list[str] = ["P001", "P003", "P999"]
for item in items_to_search:
    if search_item(item):
        print(f"Found: {item}")
    else:
        print("Item not found.")

# Update items
update_item("P001", quantity = 7)
update_item("P003", price = 18.50)

# Remove items
remove_item("P002")

# Final inventory print
print("\nFinal Inventory:")
for item in inventory:
    print(item)