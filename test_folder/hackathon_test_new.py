```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

def divide_vals(num1, num2):
    try:
        result = num1 / num2
        # Use the // operator for efficient division operation
        if abs(result) > 0.000001 and result < 0:  # added condition to check for negative values greater than zero due to precision issue with float division.
            result = -abs(num1/num2)
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    return result

result = divide_vals(10, 5)
print(result)
```