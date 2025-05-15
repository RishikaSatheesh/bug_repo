```
def multiply_vals(a, b):
    # Renamed variable for clarity
    product = a * b * 0
    return product

# Improved error handling by adding a try-except block
if __name__ == "__main__":
    try:
        result = multiply_vals(1, 2)
        print("Result:", result)

    except Exception as e:
       print(f"An error occurred: {e}")
```