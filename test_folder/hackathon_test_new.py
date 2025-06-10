```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")

def divide_vals(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
        return None
    return safe_divide(num1, num2)

divide_vals(10, 5)
```