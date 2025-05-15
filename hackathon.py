```python
#!/usr/bin/env python3

# Import required libraries
import os
from typing import List, Dict

def load_products() -> List[Dict]:
    """Load products from file"""
    try:
        with open('products.txt', 'r') as file:
            lines = [line.strip().split(',') for line in file.readlines()]
            return [{key: value for key, value in zip(line[:2], line[2:])} for line in lines]
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def add_to_cart(products: List[Dict]) -> None:
    """Add item to cart"""
    cart = []
    for i, product in enumerate(products):
        # Check if price is valid
        try:
            price = float(product['price'].replace('$', ''))
        except ValueError:
            print(f"Error: Invalid price for product {product['name']}. Skipping...")
            continue

        cart.append({
            "index": i,
            "name": product["name"],
            "price": price
        })
    return cart

def main() -> None:
    products = load_products()
    cart = add_to_cart(products)

    # Print cart
    for item in cart:
        print(f"Item {item['index']}: Name = {item['name']}, Price = ${item['price']}")

if __name__ == "__main__":
    main()
```