# Esercizio_3:
"""
 E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create functions that manage the shopping cart, allowing the user to add, remove, and view products in the cart.
    Create a function that calculates the cart total and apply any discounts or taxes.
    Create a funciton to print a detailed summary of the cart including products and totals.
    Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

"""
from typing import Any

# Function to define a product with name, price, and quantity
def create_product(name: str, price: float, quantity: int) -> dict[str, Any]:
    # Returns a dictionary representing a product
    return {
        "name": name,
        "price": price,
        "quantity": quantity
    }

# Function to add a product to the shopping cart
def add_product(cart: list[dict[str, Any]], product: dict[str, Any]) -> None:
    # Adds the product dictionary to the cart list
    cart.append(product)

# Function to remove a product from the cart by its name
def remove_product(cart: list[dict[str, Any]], product_name: str) -> list[dict[str, Any]]:
    # Creates a new list excluding the product with the specified name
    updated_cart: list[dict[str, Any]] = []
    for p in cart:
        if p['name'] != product_name:
            updated_cart.append(p)
    # Returns the updated list
    return updated_cart

# Function to view the current contents of the cart
def view_cart(cart: list[dict[str, Any]]) -> None:
    # Prints a readable list of the items in the cart
    print("Shopping Cart Contents:")
    for product in cart:
        print(f"- {product['name']}: {product['quantity']} units at €{product['price']} each")

# Function to calculate the total cost including discount and tax
def calculate_total(cart: list[dict[str, Any]], discount_rate: float = 0.10) -> dict[str, float]:
    # Compute the subtotal as the sum of (price * quantity) for each product
    subtotal: float = sum(product['price'] * product['quantity'] for product in cart)
    discount: float = discount_rate
    tax: float = 0.22  # VAT of 22%
    
    # Apply discount to subtotal
    discounted_total: float = subtotal * (1 - discount)
    # Apply tax to the discounted total
    total: float = discounted_total * (1 + tax)
    
    # Return all calculated amounts in a dictionary
    return {
        "subtotal": subtotal,
        "discount": discount * 100,  # As a percentage
        "tax": tax * 100,            # As a percentage
        "total": total
    }

# Function to print a detailed summary of the cart and totals
def print_summary(cart: list[dict[str, Any]]) -> None:
    # Print basic cart contents
    view_cart(cart)
    print("\nDetailed Summary:")
    
    # Print each product with total price
    for product in cart:
        total_price: float = product['price'] * product['quantity']  # type: ignore
        print(f"{product['name']} - Quantity: {product['quantity']}, Unit Price: €{product['price']}, Total: €{total_price}")
    
    # Calculate and print subtotal, discount, tax, and final total
    totals: dict[str, float] = calculate_total(cart)
    print("\nTotals:")
    print(f"Subtotal: €{totals['subtotal']}")
    print(f"Discount Applied: {totals['discount']}%")
    print(f"Tax: {totals['tax']}%")
    print(f"Final Total: €{round(totals['total'], 2)}")

# --- USAGE EXAMPLE ---

# Create products using the factory function
product1: dict[str, Any] = create_product("Laptop", 900.0, 1)
product2: dict[str, Any] = create_product("Mouse", 25.0, 2)
product3: dict[str, Any] = create_product("Backpack", 50.0, 1)

# Initialize an empty shopping cart
cart: list[dict[str, Any]] = []

# Add products to the cart
add_product(cart, product1)
add_product(cart, product2)
add_product(cart, product3)

# Remove the "Mouse" product from the cart
cart = remove_product(cart, "Mouse")

# Print a full summary of the cart including totals
print_summary(cart)