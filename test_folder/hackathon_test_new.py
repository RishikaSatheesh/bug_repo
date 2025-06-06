```python
def divide_values(a, b, c):
    # Try-except block for division by zero error
    try:
        result = a / b
        return result
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    
    # Use descriptive variable names and avoid duplicated code
    def divide_with_c(a, c):
        if c == 0:
            raise ValueError("Cannot divide by zero")
        return a / c
    
    try:
        result2 = divide_with_c(b, c)
        print(f"The final answer is: {result} and {result2}")
    
    except ValueError as e:
        print(e)


# Call the function with values
divide_values(10, 5, 0)

```