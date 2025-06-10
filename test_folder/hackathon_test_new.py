```python
def single_value_division(a, b, c):
    if any(x == 0 for x in [a, b, c]):
        raise ValueError("Cannot divide by zero")
    
    try:
        result = a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    
    return result

# Test the function
print(single_value_division(10, 5))  # Output: 2.0
```